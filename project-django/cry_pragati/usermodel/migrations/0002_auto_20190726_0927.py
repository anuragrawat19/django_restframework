# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-07-26 09:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermodel', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'roles'},
        ),
        migrations.AlterModelOptions(
            name='userroles',
            options={'verbose_name': 'useroles'},
        ),
    ]