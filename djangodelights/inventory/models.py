from datetime import datetime
from email.policy import default
from turtle import title
from django.db import models
from django.utils import timezone 

# Create your models here.
class Ingredient(models.Model):
    unit_choices = [("g","g"), ("kg", "kg"), ("l", "l"),("piece" ,"piece")  ]
    name = models.CharField(max_length=30)
    quantity = models.IntegerField(default=0)
    unit =  models.CharField(max_length=5, choices=unit_choices, default="piece")
    unit_price = models.FloatField(default=0.0)
    image_url = models.CharField(max_length=400, default="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Ikea-Brooklyn-Warehouse-Aisles.jpg/640px-Ikea-Brooklyn-Warehouse-Aisles.jpg")

class MenuItem(models.Model):
    title = models.CharField(max_length=30)
    item_price = models.FloatField(default=0.0)
    image_url = models.CharField(max_length=400, default="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/640px-Good_Food_Display_-_NCI_Visuals_Online.jpg")
 
class RecipeRequirement(models.Model):
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    Ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    ammount = models.FloatField(default = 1.0)

class Purchase(models.Model):
     item = models.ForeignKey(MenuItem,  on_delete=models.PROTECT)
     time_stamp = models.DateTimeField(default= timezone.now)
    
