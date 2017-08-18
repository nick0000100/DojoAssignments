# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def test(request):
    context = {
    "somekey":"somevalue"
    }
    return render(request,'time_app/index.html', context)

def index(request):
    context = {
    "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    print context
    return render(request,'time_app/index.html', context)