# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, 'survey_app/index.html')

def process(request):
    if request.method == "POST":
        try:
            request.session['count'] += 1
        except:
            request.session['count'] = 0
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect("/")

def result(request):
    return render(request, 'survey_app/process.html')

def reset(request):
    return redirect('/')

