# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return render(request, 'blogs_app/index.html')

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

def show(request, number):
    response = "placeholder to display blog" + " " + number
    return HttpResponse(response)

def edit(request, number):
    print number
    response = "placeholder to edit blog" + " " + number
    return HttpResponse(response)

def destroy(request, number):
    return redirect('/blogs')