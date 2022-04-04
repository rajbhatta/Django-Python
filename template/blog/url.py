from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', view, function_name)
    path('', views.home, name='blog-home'),

]