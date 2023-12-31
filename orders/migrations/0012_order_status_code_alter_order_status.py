# Generated by Django 4.2.5 on 2023-10-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status_code',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('processing', '25'), ('shipped', '50'), ('out for delivery', '75'), ('delivered', '100'), ('cancelled', '0')], default='processing', max_length=20),
        ),
    ]
