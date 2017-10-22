# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CityInfo (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    landmark_type = models.CharField(blank=True, max_length=30)
    landmark_pic = models.ImageField(upload_to = 'images', blank=True) 

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
    
    industry_type = models.CharField(blank=True, max_length=30)
    phone_number = models.CharField(blank=True, max_length = 15)
    unit_number = models.CharField(blank=True, max_length = 3)
    street_number = models.CharField(blank=True, max_length = 3)
    street_name = models.CharField(blank=True, max_length = 20)
    suburb = models.CharField(blank=True, max_length = 20)
    state = models.CharField(blank=True, max_length = 20)
    postcode = models.CharField(blank=True, max_length = 4)
    email = models.CharField(blank=True, max_length = 100)

    longitude = models.FloatField(blank=True, default = 0)
    latitude = models.FloatField(blank=True, default = 0)


    def __str__(self):
        return self.name


class UserProfile (models.Model):
    user = models.OneToOneField(User)

    phone_number = models.CharField(blank=True, max_length = 15)
    unit_number = models.CharField(blank=True, max_length = 3)
    street_number = models.CharField(blank=True, max_length = 3)
    street_name = models.CharField(blank=True, max_length = 20)
    suburb = models.CharField(blank=True, max_length = 20)
    state = models.CharField(blank=True, max_length = 20)
    postcode = models.CharField(blank=True, max_length = 4)
    
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
