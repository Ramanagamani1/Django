from django.urls import path
from todo import views


urlpatterns = [
    path('',views.index),
    path('lists/',views.show_lists,name="lists_page"),
    path('add_list/',views.add_list)
]
