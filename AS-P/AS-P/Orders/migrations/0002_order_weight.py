# Generated by Django 2.1.2 on 2018-11-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='weight',
            field=models.DecimalField(decimal_places=4, max_digits=10, null=True),
        ),
    ]