# Generated by Django 4.2.3 on 2023-07-26 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart_item',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
