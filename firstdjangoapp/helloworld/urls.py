from django.urls import path
from helloworld import views

urlpatterns=[
    path('',views.index, name='hello'),
    path("html/",views.hello_html),
    path('hello_all/<str:name>',views.hello)
]