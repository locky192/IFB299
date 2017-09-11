# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile (models.Model):
    user = models.OneToOneField(User)

    phone_number = models.CharField(blank=True, max_length = 15)
    #phone_number = models.IntegerField(blank=True)
    address = models.TextField(blank=True)
    
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    business = 'Business'
    student = 'Student'
    tourist = 'Tourist'

    user_type_choices = (
        (business, 'Business'),
        (student, 'Student'),
        (tourist, 'Tourist')
    )

    user_type = models.CharField(
        max_length = 8,
        choices = user_type_choices,
        default = business,
        )

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username
