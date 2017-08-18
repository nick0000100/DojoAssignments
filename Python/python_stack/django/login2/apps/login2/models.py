# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    
    # Validates the data given to create a new user
    def validateReg(self, postData):
        errors = {}
        first_name = postData["first_name"]
        last_name = postData["last_name"]
        email = postData["email"]
        password = postData["password"]
        cPass = postData["cPass"]

        # Validates the first and last name based on length and if the contain letters only.
        if len(first_name) <= 2:
            errors["first_name"] = "First name must be at least 3 characters long."
        elif not NAME_REGEX.match(first_name):
            errors["first_name"] = "First name can only contain letters."
        if len(last_name) <= 2:
            errors["last_name"] = "Last name must be at least 3 characters long."
        elif not NAME_REGEX.match(last_name):
            errors["last_name"] = "Last name can only contain letters."

        # Validates the given email based on length, if it is a correctly formated email, and if it already exist in the database.
        if len(email) <= 0:
            errors["email"] = "Email is required"
        elif not EMAIL_REGEX.match(email):
            errors["email"] = "Not a valid email"
        else:
            if len(User.objects.filter(email=postData["email"])) > 0:
                errors["email"] = "Email already exist in database"
        
        # Validates the password based on if the length is atleast 8 and if it matches the confirmed password
        if len(password) < 8:
            errors["password"] = "Password did not meet the length requirement (8)"
        elif password != cPass:
            errors["password"] = "Password did not match the confirm password"

        return errors

    # Validates the information given for login; if the email and password match an instance in the database.
    def validateLogin(self, postData):
        errors = {}
        email = postData["email"]
        password = postData["password"]
        user = User.objects.filter(email = email)
        if len(user) != 1:
            errors["email"] = "Email does not exist in database"
        else:
            if not bcrypt.checkpw(password.encode(), user[0].password.encode()):
                errors["password"] = "Incorrect username/password combination"
        return errors

    # Creates a new user from the given post data
    def createNew(self, postData):
        first_name = postData["first_name"]
        last_name = postData["last_name"]
        email = postData["email"]
        password = postData["password"]
        hashPass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name = first_name,
                            last_name = last_name,
                            email= email,
                            password = hashPass)

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()