# Generated by Django 2.1.2 on 2018-11-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0003_auto_20181103_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dispatch_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
