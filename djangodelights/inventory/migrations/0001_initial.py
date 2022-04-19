# Generated by Django 4.0.4 on 2022-04-16 15:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField(default=0)),
                ('unit', models.CharField(choices=[('g', 'g'), ('kg', 'kg'), ('l', 'l'), ('piece', 'piece')], default='piece', max_length=5)),
                ('unit_price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('item_price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeRequirement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.FloatField(default=1.0)),
                ('Ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.ingredient')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2022, 4, 16, 17, 52, 46, 258723))),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.menuitem')),
            ],
        ),
    ]
