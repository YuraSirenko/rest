# Generated by Django 5.1.2 on 2024-10-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0016_alter_customer_phone_alter_waiter_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
