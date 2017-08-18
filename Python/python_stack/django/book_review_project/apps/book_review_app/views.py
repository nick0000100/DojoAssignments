# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, "book_review_app/index.html")

def allBooks(request):
    checkLogged(request)
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    else:
        context = {
            "books": Book.objects.all(),
            "users": User.objects.all(),
            "reviews": Review.objects.all().order_by("-created_at")[:3]
        }
        return render(request, "book_review_app/books.html", context)

def singleBook(request, id):
    checkLogged(request)
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    else:
        book = Book.objects.get(id = id)
        context = {
            "book": book,
            "reviews": book.reviews.all(),
            "users": User.objects.all()
        }
        return render(request, "book_review_app/book.html", context)

def userPage(request, id):
    checkLogged(request)
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    user = User.objects.get(id = id)
    reviews = user.reviews.all()
    books = []
    for review in reviews:
        books.append(Book.objects.get(id = review.book_id))
    context = {
        "user": user,
        "count": user.reviews.count(),
        "books": books
    }
    print books
    return render(request, "book_review_app/user.html", context)

def register(request):
    errors = User.objects.validateReg(request.POST)
    if len(errors):
        errorPrinter(request, errors)
        return redirect('/')
    else:
        User.objects.createNew(request.POST)
        loggedIn(request)
        return redirect('/books')

def login(request):
    errors = User.objects.validateLogin(request.POST)
    if len(errors):
        errorPrinter(request, errors)
        return redirect('/')
    else:
        loggedIn(request)
        return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')

def addPage(request):
    checkLogged(request)
    if not request.session['loggedIn']:
        messages.error(request, "Log in to view that page.")
        return redirect('/')
    context = {
        "authors": Author.objects.all()
    }
    return render(request, "book_review_app/add.html", context)

def addBookReview(request):
    errors = User.objects.validateBookReview(request.POST)
    if len(errors):
        errorPrinter(request, errors)
        return redirect('/books/add')
    else:
        if request.POST["new_author"]:
            author = Author.objects.createAuthor(request.POST)
        else:
            author = request.POST["author"]
        book = Book.objects.createBook(request.POST, author)
        user = User.objects.get(id=request.session["id"])
        Review.objects.createReview(request.POST, book, user)
        return redirect('/book/{}'.format(book.id))

def addReview(request, id):
    book = Book.objects.get(id = id)
    user = User.objects.get(id = request.session["id"])
    Review.objects.createReview(request.POST, book, user)
    return redirect('/book/{}'.format(id))

def deleteReview(request, id):
    review = Review.objects.get(id = id)
    book_id = review.book_id
    review.delete()
    return redirect("/book/{}".format(book_id))

# Adds error messages to messages.
def errorPrinter(request, errors):
    for error, message in errors.iteritems():
        messages.error(request, message)

# Changes session data to that of the user's.
def loggedIn(request):
    user = User.objects.get(email = request.POST["email"])
    try:
        request.session['loggedIn'] = True
    except KeyError:
        request.session['loggedIn']
    try:
        request.session["id"] = user.id
    except KeyError:
        request.session["id"]
    try:
        request.session["first_name"] = user.first_name
    except KeyError:
        request.session["first_name"]

# Checks to see if the user is logged in.
def checkLogged(request):
    try:
        request.session['loggedIn']
    except KeyError:
        request.session['loggedIn'] = False