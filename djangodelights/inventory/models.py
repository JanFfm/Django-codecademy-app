from django.db import models
from datetime import datetime
# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=255,unique=True)
    price = models.PositiveIntegerField ()
    stock = models.PositiveIntegerField (default=0)
    def __str__(self):
        return self.name.title()
    class Meta:
            indexes=[models.Index(fields=['price']),models.Index(fields=['stock'])]


class MenuItem(models.Model):
    name = models.CharField(max_length=255,unique=True)
    price = models.PositiveIntegerField ()
    img_link = models.CharField(max_length=900, null=True)
    class Meta:
        indexes=[models.Index(fields=['price'])]
    
class Purchases(models.Model):
    date = models.DateTimeField()
    item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    class Meta:
        ordering= ['-date']
    def __str__(self):
        return str(self.item.name) + " ("+str(self.item.id)+") " +str(self.date)
        

class Recipe(models.Model):
    item =models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    ingredient=models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField (default=0)

