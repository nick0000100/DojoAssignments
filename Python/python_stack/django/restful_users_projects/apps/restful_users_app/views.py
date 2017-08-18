# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

# Displays the homepage with all of the users in the database.
def index(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "restful_users_app/index.html", context)

# Displays the page with the form to create a new user.
def new(request):
    return render(request, "restful_users_app/new.html")

# Displays information for a given user with a specific id.
def display(request, id):
    return render(request, "restful_users_app/display.html", {"user": User.objects.get(id = id)})

# Creates a new user in the database if all inputs are valid.
def create(request):
    # Checks the if there are errors in the given inputs
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/users/new')

    # Creates a new user in the database
    User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"])

    return redirect("/users")

# Edits an existing user's information.
def edit(request, id):
    context = {
        "user": User.objects.get(id = id)
    }
    return render(request, "restful_users_app/edit.html", context)

def update(request, id):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error, message in errors.items():
            messages.error(request, message)
        return redirect("/users/{}/edit".format(id))
    user = User.objects.get(id = id)
    user.first_name = request.POST["first_name"]
    user.last_name = request.POST["last_name"]
    user.email = request.POST["email"]
    user.save()
    return redirect("/users")

def delete(request, id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/users')