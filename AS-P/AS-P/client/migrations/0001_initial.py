# Generated by Django 2.1.2 on 2018-11-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('shipping_weight', models.DecimalField(decimal_places=4, max_digits=10, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Item')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
    ]
