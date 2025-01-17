# Generated by Django 5.1 on 2024-11-13 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_location_product_stock_stockmovement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockmovement',
            name='received',
        ),
        migrations.RemoveField(
            model_name='stockmovement',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='location',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='stockmovement',
            name='product_stock',
        ),
        migrations.DeleteModel(
            name='location',
        ),
        migrations.DeleteModel(
            name='product',
        ),
        migrations.DeleteModel(
            name='stock',
        ),
        migrations.DeleteModel(
            name='stockMovement',
        ),
    ]
