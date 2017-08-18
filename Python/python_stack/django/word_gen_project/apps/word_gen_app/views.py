# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.
def index(request):
    return render(request,'word_gen_app/index.html')

def randomWord(request):
    try:
        request.session['count'] += 1
    except:
        request.session['count'] = 1
    randWord = get_random_string(length=10)
    context = {
        "word": randWord
    }
    print context
    return render(request, 'word_gen_app/index.html', context)

def reset(request):
    request.session.clear()
    return redirect('/')