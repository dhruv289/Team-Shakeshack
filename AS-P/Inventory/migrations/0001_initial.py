# Generated by Django 2.1.2 on 2018-11-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=4)),
                ('category', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('item_id', models.DecimalField(decimal_places=0, max_digits=4)),
                ('image_name', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
