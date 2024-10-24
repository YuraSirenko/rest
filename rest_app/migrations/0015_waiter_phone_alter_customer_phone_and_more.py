# Generated by Django 5.1.2 on 2024-10-17 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0014_alter_customer_sale'),
    ]

    operations = [
        migrations.AddField(
            model_name='waiter',
            name='phone',
            field=models.CharField(default='000-000-00-00', max_length=18),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='000-000-00-00', max_length=18),
        ),
        migrations.AlterField(
            model_name='customer',
            name='sale',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.sale'),
        ),
    ]
