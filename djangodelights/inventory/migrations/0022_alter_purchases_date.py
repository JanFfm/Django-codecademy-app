# Generated by Django 4.1.7 on 2023-04-11 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_alter_purchases_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 4, 11, 15, 19, 9, 700677)),
        ),
    ]
