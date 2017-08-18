# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        "courses": Course.objects.all(),
        "descriptions": Description.objects.all()
    }
    return render(request, "courses_app/index.html", context)

def add(request):
    errors = Course.objects.validate(request.POST)
    if len(errors):
        for error, message in errors.iteritems():
            messages.error(request,message)
        return redirect('/')
    #Create new course
    Course.objects.createCourse(request.POST)
    return redirect('/')

def deletePage(request, id):
    context = {
        "course": Course.objects.get(id = id),
        "description": Description.objects.get(id = id)
    }
    return render(request, "courses_app/delete.html", context)

def deleteCourse(request, id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect("/")