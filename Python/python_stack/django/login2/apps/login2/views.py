# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *
from django.contrib import messages

# Create your views here.

def index(request):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if request.session['loggedIn']:
        return redirect('/success')
    return render(request, "login2/index.html")

def success(request):
    return render(request, "login2/success.html")

def register(request):
    errors = User.objects.validateReg(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/')
    else:
        User.objects.createNew(request.POST)
        loggedIn(request)
        return redirect('/success')

def login(request):
    errors = User.objects.validateLogin(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/')
    else:
        loggedIn(request)
        return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')

def loggedIn(request):
    try:
        request.session['loggedIn'] = True
    except KeyError:
        request.session['loggedIn']
    user = User.objects.get(email = request.POST["email"])
    try:
        request.session["first_name"] = user.first_name
    except:
        request.session["first_name"]
