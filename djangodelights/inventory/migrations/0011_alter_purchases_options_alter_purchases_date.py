# Generated by Django 4.1.7 on 2023-03-29 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_alter_purchases_date_alter_purchases_item_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchases',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='purchases',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 29, 20, 48, 0, 386350)),
        ),
    ]