from django import forms
from django.db import models

from .models import Ingredient, MenuItem, Recipe

class MenuItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
            super(MenuItemForm, self).__init__(*args, **kwargs)
            self.fields['img_link'].required = False
    class Meta:
        model = MenuItem
        fields = ['name', 'price', 'img_link']
        
        
        
class NewInventoyItemForm(forms.ModelForm):
    class Meta:
        model =  Ingredient
        fields = ['name', 'price','stock']

class InventoyItemForm(forms.ModelForm):
    class Meta:
        model =  Ingredient
        fields = ['stock']



class RecipeQuantityForm(forms.ModelForm):
    #ingredient = forms.ModelChoiceField(queryset= Ingredient.objects.all())  # hier das richtige geten!
    
    #def __init__(self, recipe,  *args, **kwargs):
    #    super( RecipeQuantityForm, self).__init__(*args, **kwargs)
    #    print(recipe.id)        
        
    #ing_id = 
    class Meta:
        model = Recipe
        fields = ['quantity']
        info = {'ingredient': forms.HiddenInput()}
        


class RecipeAddIngForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset= Ingredient.objects.all() ,to_field_name="id")
    
    class Meta:
        model = Recipe
        fields = ['quantity']
        
    #def label_from_instance(self, obj):
    #    return "Menu #%s) %s" % (obj.id,obj.name)
        