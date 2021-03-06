"""practice_2 URL Configuration

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
    print "@@@@@@@@@"

urlpatterns = [
    url(r'^$', views.highscores),
    url(r'^play$', views.play),
    url(r'^process$', views.process),
    url(r'^dashboard$', views.dashboard),
    url(r'^user/(?P<id>\d+)$', views.userPage)
    
]
