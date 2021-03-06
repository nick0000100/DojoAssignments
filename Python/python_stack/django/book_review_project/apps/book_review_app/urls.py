"""book_review_project URL Configuration

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
    print "###########@@@@@@@@@"

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^books$', views.allBooks),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^books/add$', views.addPage),
    url(r'^bookReview$', views.addBookReview),
    url(r'^book/(?P<id>\d+)$', views.singleBook),
    url(r'^addReview/(?P<id>\d+)$', views.addReview),
    url(r'^delete/(?P<id>\d+)$', views.deleteReview),
    url(r'^user/(?P<id>\d+)$', views.userPage),
]
