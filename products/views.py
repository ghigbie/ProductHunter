from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

title = 'Product Hunter'

def home(request):
    return render(request, 'products/home.html',
                 {'title' : title,
                 'products': 'products'})

def products(request):
    return render(request, 'products/products',
                 {'title' : title,
                  'products': [1, 2, 3, 4, 5]})

def create(request):
    return render(request, 'produts/create.html')
