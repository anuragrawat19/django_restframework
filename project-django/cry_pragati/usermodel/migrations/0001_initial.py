# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2019-07-26 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'message': 'This role already exists '}, max_length=100, unique=True)),
                ('code', models.CharField(blank=True, max_length=8, null=True)),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='usermodel.Roles')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='username', to='usermodel.Roles')),
            ],
            options={
                'db_table': 'userrole',
            },
        ),
    ]