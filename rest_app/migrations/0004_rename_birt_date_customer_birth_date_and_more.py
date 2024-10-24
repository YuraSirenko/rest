# Generated by Django 5.1.2 on 2024-10-15 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0003_alter_order_event_started_alter_tableinrestaurant_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='birt_date',
            new_name='birth_date',
        ),
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='birth_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='hire_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='waiter',
            name='last_name',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
