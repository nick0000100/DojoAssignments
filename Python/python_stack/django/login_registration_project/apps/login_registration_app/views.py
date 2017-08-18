# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if request.session['loggedIn']:
        return redirect('/success')
    else:
        return render(request, "login_registration_app/index.html")

def displaySuccess(request):
    context = {
        "user": User.objects.get(email = request.POST['email'])
    }
    return render(request, "login_registration_app/success.html")

def register(request):
    errors = User.objects.validateReg(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/')
    else:
        User.objects.createNew(request.POST)
        loggedIn(request)
        context = {
            "user": User.objects.get(email = request.POST['email'])
        }
        return render(request, "login_registration_app/success.html", context)

def login(request):
    errors = User.objects.validateLogin(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request, message)
        return redirect('/')
    else:
        loggedIn(request)
        context = {
            "user": User.objects.get(email = request.POST['email'])
        }
        return render(request, "login_registration_app/success.html", context)

def loggedIn(request):
    try:
        request.session['loggedIn'] = True
    except KeyError:
        request.session['loggedIn']