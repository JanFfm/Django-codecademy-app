from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('inventory/', views.inventory, name='inventory'),
    path('menu/', views.menu, name='menu'),
    path('purchases/', views.purchases, name='purchases'),
    path('recipes/', views.recipes, name='recipes'),
    
    path('update_inventory_item/<int:id>', views.update_inventory_item, name='update_inventory_item'),
    path('submit_item_change/<int:id>', views.submit_item_change, name='submit_item_change'),    
    path('add_inventory_item', views.add_inventory__item, name='add_inventory__item'),    
    path('submit/add_inventory_item', views.submit_new_inventory_item, name='submit_new_inventory_item'),
    path('delete_inventory_item', views.delete_inventory_item, name='delete_inventory_item'),    


    path('add_menu_item', views.add_menu_item, name='add_menu_item'),
    path('submit/new_menu_item', views.submit_new_menu_item, name='submit_new_menu_item'),


    path('edit_recipe/<int:id>', views.edit_recipe, name='edit_recipe'),
    path('submit/recipe_change/<str:type>/<int:target_id>', views.submit_recipe_change, name='submit_recipe_change'),



    path('make_purchase/<int:id>', views.make_purchase, name='make_purchase'),




    path('item/<int:id>/', views.menu_item_page, name='item_page'),
    
    #path('purchase_item', views.purchase_item, name="purchase_item"),
    path('calcs', views.calcs, name="calcs"),

    
]