from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name="home"),
  path('inventory', views.inventory_list.as_view(), name="inventory"),
  path('menu-items', views.MenuItem_list.as_view(), name="menu"),
  path('recipe-list', views.recipe_list.as_view(), name="recipes"),
  path('purchases', views.Purchase_list.as_view(), name="purchases")




]


