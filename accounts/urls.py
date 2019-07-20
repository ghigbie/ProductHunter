from django.urls import path 
from . import views

urlpatterrns = [
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='loguout')
]