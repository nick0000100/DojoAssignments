# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData["first_name"]) <= 0:
            errors["first_name"] = "First name is required"
        elif not NAME_REGEX.match(postData["first_name"]):
            errors["first_name"] = "First name can not contain non letters"
        if len(postData["last_name"]) <= 0:
            errors["last_name"] = "Last name is required"
        elif not NAME_REGEX.match(postData["last_name"]):
            errors["last_name"] = "Last name can not contain non letters"
        if len(postData["email"]) <= 0:
            errors["email"] = "Email is required"
        elif not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Not a valid email"
        else:
            if len(self.filter(email=postData["email"])) > 0:
                errors["email"] = "Email already exist in database"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()