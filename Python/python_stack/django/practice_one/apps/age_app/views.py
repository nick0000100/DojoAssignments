# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from models import *
from ..login_app.models import User
from django.contrib import messages

# Create your views here.

def index(request):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    else:
        context = {
            "0-10": User.objects.filter(ageRange = "0-10").count(),
            "11-18": User.objects.filter(ageRange = "11-18").count(),
            "19-24": User.objects.filter(ageRange = "19-24").count(),
            "24-35": User.objects.filter(ageRange = "24-35").count(),
            "36-50": User.objects.filter(ageRange = "36-50").count(),
            "50+": User.objects.filter(ageRange = "50+").count(),
            "top3": []
        }

        max = None
        while len(context["top3"]) < 3:
            for key in context:
                if key != "top3":
                    if max == None or context[key] > max["count"]:
                        max = {"name": key, "count": context[key]}
            context["top3"].append(max)
            del context[max["name"]]
            max = None

        return render(request, "age_app/dashboard.html", context)

def ageDash(request, low, up):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    else:
        if int(low) == 51:
            users = User.objects.filter(ageRange = "50+")
        else:
            users = User.objects.filter(ageRange = "{}-{}".format(low, up))
        allComments = Comment.objects.all()
        comments = []
        # Gets comments by users in the age range
        for user in users:
            for comment in allComments:
                if comment.user_id == user.id:
                    comments.append(comment)
        if request.session["age"] <= int(up) and request.session["age"] >= int(low):
            ableAdd = True
        else:
            ableAdd = False
        context = {
            "name": "{}-{}".format(low, up),
            "users": users,
            "comments": comments,
            "low": low,
            "up": up,
            "ableAdd": ableAdd
        }
        return render(request, "age_app/ageDash.html", context)

def add(request, low, up):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    else:
        context = {
            "low": low,
            "up": up
        }
        return render(request, "age_app/comment.html", context)

def newComment(request, low, up):
    user = User.objects.filter(name = request.session["name"]).filter(age = request.session["age"])[0]
    comment = Comment.objects.newComment(request.POST, user)
    return redirect('/users/groups/{}/{}'.format(low, up))