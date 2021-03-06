# Generated by Django 2.1.2 on 2018-11-07 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0001_initial'),
        ('users', '0001_initial'),
        ('Location_Data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=4)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.DecimalField(decimal_places=2, max_digits=4)),
                ('status', models.CharField(max_length=200)),
                ('priority', models.CharField(max_length=200)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('dispatch_time', models.DateTimeField(blank=True, null=True)),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Location_Data.Location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
        ),
        migrations.AddField(
            model_name='content',
            name='orderID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Orders.Order'),
        ),
        migrations.AddField(
            model_name='content',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]
