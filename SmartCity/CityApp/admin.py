# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from CityApp.models import UserProfile, CityInfo

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(CityInfo)

