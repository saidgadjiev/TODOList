# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_todo_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
