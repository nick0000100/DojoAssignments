# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random
import datetime


# Create your views here.
def index(request):
    return render(request, 'ninja_gold_app/index.html')

def process(request):
    try:
        request.session['gold']
    except:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except:
        request.session['activities'] = []
    dateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if request.POST['building'] == 'farm':
        gold = random.randrange(10,21)
        activity = "Earned {} gold from the farm {}".format(str(gold), dateTime)
        request.session['gold'] += gold
    elif request.POST['building'] == 'cave':
        gold = random.randrange(5,11)
        activity = "Earned {} gold from the cave {}".format(str(gold), dateTime)
        request.session['gold'] += gold
    elif request.POST['building'] == 'house':
        gold = random.randrange(2,6)
        activity = "Earned {} gold from the house {}".format(str(gold), dateTime)
        request.session['gold'] += gold
    elif request.POST['building'] == 'casino':
        gold = random.randrange(0,51)
        gomble = random.randint(0,1)
        if gomble == 0:
            request.session['gold'] += gold
            activity = "Earned {} gold from the casino {}".format(str(gold), dateTime)
        else:
            request.session['gold'] -= gold
            activity = "Lost {} gold from the casino {}".format(str(gold), dateTime)
    request.session['activities'].insert(0, activity)
    return redirect('/')

def reset(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')