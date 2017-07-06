#!/usr/bin/env python 2.7.12
#coding=utf-8
#author=yexiaozhu

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]