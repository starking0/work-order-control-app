# Generated by Django 5.1 on 2024-08-31 03:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeneralStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority_num', models.CharField(max_length=16)),
                ('days', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_type', models.CharField(max_length=32)),
                ('next_step', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='ShiftHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shift_workers', to='orders.shift')),
            ],
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_of_order', models.IntegerField()),
                ('description', models.TextField(max_length=256)),
                ('area', models.CharField(max_length=32)),
                ('carried_by', models.CharField(max_length=32)),
                ('authorized_by', models.CharField(max_length=32)),
                ('num_of_pieces', models.PositiveIntegerField()),
                ('assignment_date', models.DateField()),
                ('need_material', models.BooleanField(default=False)),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('received_by', models.CharField(blank=True, max_length=64, null=True)),
                ('delivered_by', models.CharField(blank=True, max_length=32, null=True)),
                ('current_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_work_orders', to='orders.generalstatus')),
                ('priority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='priority_work_orders', to='orders.priority')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='serviced_orders', to='orders.servicetype')),
            ],
        ),
        migrations.CreateModel(
            name='CutOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_cut_order', models.PositiveIntegerField()),
                ('material_type', models.CharField(max_length=128)),
                ('material_quantity', models.CharField(max_length=128)),
                ('request_date', models.DateField()),
                ('delivery_date', models.DateField(blank=True, null=True)),
                ('material_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('observation', models.TextField(blank=True, max_length=256)),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cut_orders', to='orders.workorder')),
            ],
        ),
        migrations.CreateModel(
            name='AssignedWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_processes', models.TextField(max_length=256)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shift_assigned_works', to='orders.shift')),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='operator_assigned_works', to='orders.worker')),
                ('work_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_works', to='orders.workorder')),
            ],
        ),
    ]