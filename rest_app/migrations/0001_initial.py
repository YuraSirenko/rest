# Generated by Django 5.1.2 on 2024-10-15 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45, null=True)),
                ('phone', models.CharField(max_length=18)),
                ('birt_date', models.DateField()),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('item_type', models.IntegerField()),
                ('quantity_in_stock', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'item_type',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('payment_type', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'payment_method',
            },
        ),
        migrations.CreateModel(
            name='SalaryType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fixed', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('percent', models.FloatField(default=0.0)),
            ],
            options={
                'db_table': 'salary_type',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sale_type', models.CharField(blank=True, max_length=45)),
                ('sale_percent', models.FloatField()),
            ],
            options={
                'db_table': 'sale',
            },
        ),
        migrations.CreateModel(
            name='TableInRestaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=45, null=True)),
                ('is_taken', models.SmallIntegerField(default=0)),
            ],
            options={
                'db_table': 'table_in_restaurant',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('number_of_customers', models.IntegerField(default=1)),
                ('total_sum', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('event_started', models.DateTimeField(auto_now_add=True)),
                ('event_ended', models.DateTimeField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.customer')),
                ('payment_method', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.paymentmethod')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.tableinrestaurant')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.AddField(
            model_name='customer',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.sale'),
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('birth_date', models.CharField(max_length=45)),
                ('hire_date', models.CharField(max_length=45)),
                ('salary_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.salarytype')),
            ],
            options={
                'db_table': 'waiter',
            },
        ),
        migrations.CreateModel(
            name='SalaryHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('total_earned', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('salary_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.salarytype')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.waiter')),
            ],
            options={
                'db_table': 'salary_history',
            },
        ),
        migrations.CreateModel(
            name='WaiterHasOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.order')),
                ('waiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.waiter')),
            ],
            options={
                'db_table': 'WaiterHasOrder',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='waiters',
            field=models.ManyToManyField(through='rest_app.WaiterHasOrder', to='rest_app.waiter'),
        ),
        migrations.CreateModel(
            name='ItemHasOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.order')),
            ],
            options={
                'db_table': 'item_has_order',
                'unique_together': {('order', 'item')},
            },
        ),
    ]
