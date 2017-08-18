# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
AGE_REGEX = re.compile(r'^[0-9]+$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        name = postData["name"]
        age = postData["age"]
        if len(name) <= 0:
            errors["name"] = "Name is required."
        elif not NAME_REGEX.match(name):
            errors["name"] = "Name can only contain letters."
        if len(age) <= 0:
            errors["age"] = "Age is required."
        elif not AGE_REGEX.match(age):
            errors["age"] = "Age must be a positive number"
        if len(User.objects.filter(name = name).filter(age = age)) > 0:
            errors["used"] = "Name and age combination already exist."
        return errors

    def newUser(self, postData):
        age = int(postData["age"])
        if age >= 0 and age <= 10:
            userRange = "0-10"
        elif age >= 11 and age <= 18:
            userRange = "11-18"
        elif age >= 19 and age <= 24:
            userRange = "19-24"
        elif age >= 25 and age <= 35:
            userRange = "24-35"
        elif age >= 36 and age <= 50:
            userRange = "36-50"
        else:
            userRange = "50+"
        user = User.objects.create(name = postData["name"],
                            age = int(postData["age"]),
                            ageRange = userRange
        )
        return user

class User(models.Model):
    name = models.CharField(max_length=255)
    ageRange = models.CharField(max_length=255)
    age = models.IntegerField()
    objects = UserManager()