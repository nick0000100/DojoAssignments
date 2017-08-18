# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.

items = [
    {
        "id": 1,
        "name": "Dog",
        "price": 19.99,
    },
    {
        "id": 2,
        "name": "Cat",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Fish",
        "price": 4.99
    },
    {
        "id": 4,
        "name": "Bear",
        "price": 49.99
    }
]

def index(request):
    context = {
        'items': items
    }
    request.session['newCharge'] = 0
    return render(request, "amazon_app/index.html", context)

def process(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            newCharge = item['price'] * int(request.POST['quantity'])
        try:
            request.session['spent']
        except:
            request.session['spent'] = 0
        try:
            request.session['itemNumber']
        except:
            request.session['itemNumber'] = 0
        try:
            request.session['newCharge']
        except:
            request.session['newCharge'] = 0

    request.session['spent'] += newCharge
    request.session['itemNumber'] += int(request.POST["quantity"])
    request.session['newCharge'] = newCharge
    return redirect('/checkout')

def checkout(request):
    return render(request, 'amazon_app/checkout.html')