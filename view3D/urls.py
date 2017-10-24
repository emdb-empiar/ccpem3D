'''
Created on 24 Oct 2017

@author: pkorir
'''
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    ]