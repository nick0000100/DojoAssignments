# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def users(request):
    response = "placeholder to later display all the list of users"
    return HttpResponse(response)

def new(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)