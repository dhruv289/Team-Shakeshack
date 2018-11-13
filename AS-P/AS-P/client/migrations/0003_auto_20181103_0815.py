# Generated by Django 2.1.2 on 2018-11-03 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_cart_shipping_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='shipping_weight',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]