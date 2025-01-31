# Generated by Django 5.1 on 2024-11-19 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_stockmovement_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockmovement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product', to_field='identifier'),
        ),
    ]
