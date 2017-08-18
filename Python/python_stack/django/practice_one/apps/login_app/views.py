# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import *
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "login_app/index.html")

def login(request):
    errors = User.objects.validate(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/')
    else:
        User.objects.newUser(request.POST)
        loggedIn(request)
        return redirect('/users')

def logout(request):
    request.session.flush()
    return redirect('/')

def loggedIn(request):
    user = User.objects.filter(name = request.POST["name"]).filter(age = request.POST["age"])[0]
    try:
        request.session['loggedIn'] = True
    except KeyError:
        request.session['loggedIn']
    try:
        request.session["age"] = int(user.age)
    except KeyError:
        request.session["age"]
    try:
        request.session["name"] = user.name
    except KeyError:
        request.session["fname"]