from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Ingredient, MenuItem, RecipeRequirement,Purchase

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Hello HttpResponse</h1>')    

     return render(request, 'inventory/home.html')

class inventory_list(ListView):
    model = Ingredient
    template_name = 'inventory/ingredients-list.html'

class MenuItem_list(ListView):
    model = MenuItem
    template_name = 'inventory/items-list.html'
class recipe_list(ListView):
    model = RecipeRequirement
    template_name = 'inventory/recipe-list.html'

class Purchase_list(ListView):
    model = Ingredient
    template_name = 'inventory/purchases-list.html'