from django.contrib import admin
from django.urls import  path
from isnewyear import views

urlpatterns = [
    path('', views.index),
    path('<str:name>',views.index)
]
