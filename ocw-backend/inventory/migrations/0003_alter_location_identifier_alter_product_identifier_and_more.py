# Generated by Django 5.1 on 2024-11-15 23:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_stockmovement_cuantity_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='identifier',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='identifier',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.location', to_field='identifier'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.product', to_field='identifier'),
        ),
    ]
