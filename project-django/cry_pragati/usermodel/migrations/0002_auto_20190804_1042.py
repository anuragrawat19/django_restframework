# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2019-08-04 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persontasks',
            name='startdate',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]