# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CityApp', '0009_auto_20171021_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cityinfo',
            name='picture',
        ),
    ]
