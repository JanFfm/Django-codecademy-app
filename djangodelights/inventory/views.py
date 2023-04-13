from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from  .models import MenuItem, Purchases, Ingredient, Recipe
from .forms import InventoyItemForm,NewInventoyItemForm, MenuItemForm, RecipeQuantityForm, RecipeAddIngForm
from .helpers import build_recipe_list, get_recipe
from django.core.exceptions import BadRequest
from django.contrib import messages as msg


from django.db import DatabaseError
from django.contrib.auth.decorators import login_required


from datetime import datetime

from PIL import Image
import requests as req
from io import BytesIO


def front_page(request):
    return render(request, 'inventory/frontpage.html')


#################show database entries:

def menu(request):
    menus = MenuItem.objects.all().values()
    context = {'items': menus}
    return render (request, 'inventory/menu.html', context)

@login_required
def inventory(request):
    template = 'inventory/inventory.html'
    ingredients = Ingredient.objects.all().values()
    context = {'ingredients': ingredients}

    return render(request, template, context)


@login_required
def purchases(request):
    ####ToDO: test inventory/ update inventory
    template = 'inventory/purchases.html'
    purchases = Purchases.objects.all().values()
    for p in purchases:
        menu_item = MenuItem.objects.get(pk=p['item_id'])
        print(menu_item.name)
        p['item_name'] = menu_item.name
    print(purchases)
    context = {'purchases': purchases}
    return render(request, template, context)


@login_required
def recipes(request):
    template = 'inventory/recipes.html'
    recipe_list = build_recipe_list()    
    return render(request, template, {'menu_item': recipe_list})

##################details pages:

def menu_item_page(request, id):
    """ Shows details page for a menu item

    Args:
        request (_type_): _description_
        id (int): menu item id

    Returns:
        _type_: _description_
    """
    template = 'inventory/item_page.html'
    item = MenuItem.objects.get(pk=id)
    recipe =get_recipe(id)
    context = {'item': item, 'recipe':recipe }
    return render(request, template, context)

#################modify models.Inventory:

@login_required
def add_inventory__item(request):
    form = NewInventoyItemForm()
    return render(request, 'inventory/add_inventory_item.html', {'form': form})

@login_required
def submit_new_inventory_item(request):
        if request.method == 'POST':
            print ("write to db:", request.POST)
         
            print("redirect to:", request.META['HTTP_REFERER'])
            try:
                item = Ingredient(name=str(dict(request.POST)['name'][0]).title(), price=dict(request.POST)['price'][0], stock=dict(request.POST)['stock'][0])
                item.save()
            except Exception as error:
                msg.error(request, error)
                return redirect('add_inventory__item')

            msg.success(request,"Added " + str(dict(request.POST)['name'][0]) +" to stock")
            return redirect("inventory")
    
        msg.error(request, 'Invalid request.')
        return redirect('add_inventory__item')


@login_required
def delete_inventory_item(request):
    try:
        if len(Recipe.objects.filter(ingredient=Ingredient.objects.get(pk=str(request.POST['id'])))) > 0:
            msg.error(request, "Ingredient is part of " + str(len(Recipe.objects.filter(ingredient=Ingredient.objects.get(pk=str(request.POST['id']))))) + " recipes! Can not be removed!")
        else:      
            Ingredient.objects.get(pk=str(request.POST['id'])).delete()
        
    except Exception as error:
        msg.error(request, error)
    return redirect('inventory')

@login_required
def update_inventory_item(request, id):
    template = 'inventory/update_inventory.html'
    ing = Ingredient.objects.get(pk=id)
    form = InventoyItemForm(instance=Ingredient.objects.get(pk=id))
    context = {'ing':ing, 'form': form}
    return render(request, template, context)

@login_required
def submit_item_change(request, id):
    """ change the stock of an item in inventory """
    if request.method == 'POST':
        print ("write to db:", request.POST)
        new_stock = dict(request.POST)['stock'][0]
        print("redirect to:", request.META['HTTP_REFERER'])
        try:
            new_stock = dict(request.POST)['stock'][0]

            Ingredient.objects.filter(pk=id).update(stock=new_stock)
        except:
            msg.error(request, "DB error")
            raise DatabaseError


        msg.success(request, "stock changed")
        return redirect(request.META['HTTP_REFERER'])
    
    msg.error(request, "Bad request")
    raise BadRequest('Invalid request.')

        
################modify models.MenuItem:
@login_required        
def add_menu_item(request):
    form = MenuItemForm()
    return render(request, 'inventory/add_menu_item.html', {'form': form})

@login_required
def submit_new_menu_item(request):
    try:
        new_item_dict = dict(request.POST)   
        img_link = new_item_dict['img_link'][0]
        try:
            r = req.get(img_link)
            im = Image.open(BytesIO(r.content))
            im.close()
        except:
            if not (img_link == "" or img_link == None):
                msg.error(request, "Image from link could not be read!")
        img_link= None
        item= MenuItem(name= str(new_item_dict['name'][0]).title(), price=new_item_dict['price'][0], img_link=img_link)
        item.save()
        id = item.id
        print(id)


        msg.success(request, "Added Item to menu.")
        return redirect('edit_recipe', id=id)
    except Exception as e:
        msg.error(request, e)    
    return redirect(request.META['HTTP_REFERER'])




#####modify recipes
@login_required
def edit_recipe(request, id):
    recipe =get_recipe(id) 
    menu_item = MenuItem.objects.get(pk=id)  
    form = RecipeAddIngForm()
    return render(request, 'inventory/update_recipe.html', {'id': id,'recipe': recipe, 'form': form, 'menu_item':menu_item.name})

@login_required
def submit_recipe_change(request, type, target_id):
    if type == 'change':
        try:
            post = dict(request.POST)
            print(post)
            quantity = int(post['quantity'][0])
            if quantity==0:
                obj = Recipe.objects.filter(pk=target_id)
                obj.delete()
                msg.success(request, "Object deleted.")

            else:
                print(target_id)
                i = Recipe.objects.get(pk=target_id)
                i.quantity= quantity
                i.save()
            
        
        except Exception as e:
            print(e)
    elif type=='add':
        print('add')
        try:
            post = dict(request.POST)
            print(post)

            quantity = int(post['quantity'][0])
            ingredient_id= int(post['ingredient'][0])
            """ToDo: chekc if ingredient is in list
            """
            try:
                recipe = Recipe.objects.get(item=MenuItem.objects.get(pk=int(target_id)), ingredient=ingredient_id)
                msg.warning(request, "Ingredient allready part of recipe")

            except:         
                if quantity > 0:
                    x = Recipe(item=MenuItem.objects.get(pk=int(target_id)), ingredient=Ingredient.objects.get(pk=ingredient_id), quantity=quantity)
                    print(x)
                    x.save()
                    msg.success(request, "Object saved")

                else:
                    msg.warning(request, "cannot add ammount of 0 as value")
        except Exception as e:
            msg.error(request, e)

    return redirect(request.META['HTTP_REFERER'])


def make_purchase(request, id):
    purchase_time = datetime.now()
    item = MenuItem.objects.get(pk=id)
    name = item.name
    recipe=Recipe.objects.filter(item=item)
    changes = []
    for r in recipe:       
        obj = Ingredient.objects.get(name=r.ingredient)        
        if obj.stock >= r.quantity:
            obj.stock -= r.quantity
            changes.append(obj)
        else:
            msg.error(request, "Not enough items in inventory!")
            return redirect("purchases")        
    for obj in changes:
        obj.save()  
    
    p = Purchases(item=MenuItem.objects.get(pk=id), date=purchase_time)
    p.save()
    msg.success(request, str(name) + " was added to puchases-list")  
    
       
    
    return redirect("purchases")


@login_required
def calcs(request):
    purchases = Purchases.objects.all()
    total_revenue = 0
    total_cost = 0 
    for p in purchases:
        total_revenue += p.item.price
        recipe_objs = Recipe.objects.filter(item=p.item)
        for r in recipe_objs:
            ing_price = Ingredient.objects.get(name=r.ingredient).price
            price = ing_price * r.quantity
            total_cost += price        

    profit = total_revenue - total_cost
    
    template ="inventory/calcs.html"
    context = {'revenue':total_revenue, 'costs':total_cost, 'profit': profit}
    return render(request, template,context)

