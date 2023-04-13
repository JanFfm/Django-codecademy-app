# Generated by Django 4.1.7 on 2023-03-23 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_menuitem_img_link_alter_purchases_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='price',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 15, 55, 7, 680758)),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
