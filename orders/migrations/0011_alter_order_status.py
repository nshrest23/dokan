# Generated by Django 4.2.5 on 2023-10-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', '25'), ('shipped', '50'), ('out for delivery', '75'), ('delivered', '100'), ('cancelled', '0')], default='PENDING', max_length=20),
        ),
    ]
