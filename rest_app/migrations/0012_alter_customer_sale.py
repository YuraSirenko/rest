# Generated by Django 5.1.2 on 2024-10-15 22:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0011_alter_customer_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='sale',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='rest_app.sale'),
        ),
    ]
