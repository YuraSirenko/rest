# Generated by Django 5.1.2 on 2024-10-17 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0015_waiter_phone_alter_customer_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=18),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='phone',
            field=models.CharField(max_length=18),
        ),
    ]