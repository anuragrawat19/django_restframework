# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-07-30 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0008_employeedesignations_employees'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedesignations',
            name='designation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='designation', serialize=False, to='usermodel.Employees'),
        ),
    ]
