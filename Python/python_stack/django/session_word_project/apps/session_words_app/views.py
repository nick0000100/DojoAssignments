# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

def add(request):
    newWord = {}
    newWord['word'] = request.POST['word']
    newWord['color'] = request.POST.get('color')
    newWord['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    if 'size' in request.POST:
        newWord['font'] = "30pt"
    else:
        newWord['font'] = ""
    try:
        request.session['allWords']
    except:
        request.session['allWords'] = []
    allWords = request.session['allWords']
    allWords.append(newWord)
    request.session['allWords'] = allWords
    return redirect('/')

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect('/')