from django.urls import path
from . import views
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
]
