# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CityApp', '0005_auto_20170915_1503'),
    ]

    operations = [
        migrations.AddField(
            model_name='cityinfo',
            name='latitude',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='longitude',
            field=models.FloatField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cityinfo',
            name='street_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='street_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
