# Generated by Django 4.2.5 on 2023-10-18 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_rename_shipping_amount_order_shipping_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoice_id',
            field=models.CharField(default='0000000', max_length=7),
        ),
    ]
