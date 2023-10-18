# Generated by Django 4.2.5 on 2023-10-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_order_invoice_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', 'processing'), ('shipped', 'shipped'), ('out for delivery', 'out_for_delviery'), ('delivered', 'delivered'), ('cancelled', 'cancelled')], default='PENDING', max_length=20),
        ),
    ]
