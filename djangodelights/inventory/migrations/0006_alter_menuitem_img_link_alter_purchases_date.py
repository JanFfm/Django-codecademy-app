# Generated by Django 4.1.7 on 2023-03-23 14:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_ingredient_stock_alter_purchases_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='img_link',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 23, 15, 39, 39, 338958)),
        ),
    ]
