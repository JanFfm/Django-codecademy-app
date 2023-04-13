from  .models import MenuItem, Purchases, Ingredient, Recipe
from .forms import InventoyItemForm,NewInventoyItemForm, MenuItemForm, RecipeQuantityForm



from django.forms.models import model_to_dict


def build_recipe_list():
    """Querys a list of recipes for all menu items

    Returns:
        list: lsit of recipes
    """
    menu_items = MenuItem.objects.all().values()
    recipe_list= []
    counter = 0
    for i in menu_items:
        recipe_list.append( {'name': i['name'], 'id': i['id'], 'ings':[]})
      
        
        recipe = Recipe.objects.filter(item=i['id']).values()
        
        for r in recipe:
            try:
                ing = Ingredient.objects.get(pk=r['ingredient_id'])
                form =  RecipeQuantityForm(r)
                ing = model_to_dict(ing)
                item =  (ing['name'], r['quantity'],form, r['id'])
                recipe_list[counter]['ings'].append(item) 
                
            except Exception as error:
                print(error)     
        counter +=1
    
    return recipe_list


def get_recipe(menu_item_id: int):
    """_summary_

    Args:
        menu_item_id (int): pk of menu item

    Returns:
        list: ingreditens
    """
    recipe = Recipe.objects.filter(item=menu_item_id).values()
    ings = []
    for r in recipe:
            try:
                ing = Ingredient.objects.get(pk=r['ingredient_id'])
                form =  RecipeQuantityForm(r)
                ing = model_to_dict(ing)
                item =  (ing['name'], r['quantity'], form, r['ingredient_id'], r['id'])
                ings.append(item) 
            except Exception as error:
                print(error)     
    return ings