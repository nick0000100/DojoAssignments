# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def test(request):
    print "This is views"
    return render(request, 'home_app/index.html')