from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view, name='view'),
    path('create/', views.create, name='create'),
    path('edit/', views.edit, name='edit'),
    path('delete/', views.delete, name='delete'),
]