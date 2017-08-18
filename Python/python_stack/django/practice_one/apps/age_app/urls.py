# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
"""practice_one URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

def test(request):
    print "@@@@@@@@@@@@@@@@@"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^groups/(?P<low>\d+)/(?P<up>\d+)$', views.ageDash),
    url(r'^add/(?P<low>\d+)/(?P<up>\d+)$', views.add),
    url(r'^newComment/(?P<low>\d+)/(?P<up>\d+)$', views.newComment),
]
