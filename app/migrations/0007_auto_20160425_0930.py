# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20160425_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='deadline_date',
            field=models.DateField(),
        ),
    ]