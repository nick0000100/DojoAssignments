# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validateReg(self, postData):
        errors = {}
        first_name = postData["first_name"]
        last_name = postData["last_name"]
        alias = postData["alias"]
        email = postData["email"]
        password = postData["password"]
        cPass = postData["cPass"]

        # Validates the name of the user.
        if len(first_name) <= 2:
            errors['first_name'] = "First name mush be at least 2 characters long."
        elif not NAME_REGEX.match(first_name):
            errors['first_name'] = "First must only contain letters"
        if len(last_name) <= 2:
            errors['last_name'] = "Last name mush be at least 2 characters long."
        elif not NAME_REGEX.match(last_name):
            errors['last_name'] = "Last name must only contain letters"

        # Validates the alias from the user.
        if len(alias) <= 2:
            errors['alias'] = "Alias mush be at least 2 characters long."
        elif not NAME_REGEX.match(alias):
            errors['alias'] = "Name must only contain letters"

        # Validates the given password from the user.
        if len(password) < 8:
            errors['password'] = "Password is not long enough."
        elif password != cPass:
            errors["password"] = "Password and password confirmation did not match."

        return errors

    def validateLogin(self, postData):
        errors = {}
        email = postData['email']
        password = postData['password']
        user = User.objects.filter(email = email)
        if len(user) != 1:
            errors["email"] = "Email does not exist in the database."
        else:
            if not bcrypt.checkpw(password.encode(), user[0].password.encode()):
                errors["password"] = "Incorrect username/password combination."
        return errors

    def validateBookReview(self, postData):
        errors = {}
        title = postData["title"]
        review = postData["review"]
        if len(title) <= 0:
            errors["title"] = "Please enter the title of the book."
        if len(review) <=0:
            errors["review"] = "Please eneter a review for the book."
        return errors

    def createBook(self, postData, author):
        title = postData["title"]
        review = postData["review"]
        if postData["new_author"]:
            book = Book.objects.create(name = title,
                                author = author
            )
        else:
            oldAuthor = Author.objects.get(name = postData["author"])
            book = Book.objects.create(name = title,
                                author = oldAuthor
            )
        return book

    def createReview(self, postData, book, user):
        review = postData["review"]
        rating = postData["rating"]
        Review.objects.create(content = review,
                                rating = rating,
                                book = book,
                                user = user
        )

    def createAuthor(self, postData):
        name = postData["new_author"]
        author = Author.objects.create(name = name)
        return author

    def createNew(self, postData):
        first_name = postData["first_name"]
        last_name = postData["last_name"]
        alias = postData["alias"]
        email = postData["email"]
        password = postData["password"]
        hashPass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name = first_name,
                            last_name = last_name,
                            alias = alias,
                            email = email,
                            password = hashPass
        )

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()

class Author(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(Author, related_name = "authors")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    book = models.ForeignKey(Book, related_name = "reviews")
    user = models.ForeignKey(User, related_name = "reviews")
    objects = UserManager()
