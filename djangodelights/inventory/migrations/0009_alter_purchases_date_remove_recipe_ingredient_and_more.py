# Generated by Django 4.1.7 on 2023-03-23 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_alter_ingredient_price_alter_ingredient_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 16, 5, 52, 670421)),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='ingredient',
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredient',
            field=models.ManyToManyField(to='inventory.ingredient'),
        ),
    ]