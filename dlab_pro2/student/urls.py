from django.contrib import admin
from django.urls import path
from student import views
urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('add',views.add),
    path('save',views.save),
    path('show',views.show),
    path('edit/<int:id>',views.edit),
    path('delete/<int:id>',views.delete)
]
