# Generated by Django 4.2.5 on 2023-10-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_prooduct_cart_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='shipping_cost',
            field=models.FloatField(default=0),
        ),
    ]
