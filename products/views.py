from django.shortcuts import render, get_object_or_404

title = 'Product Hunter'

def home(request):
    return render(request, 'products/home.html',
                 {'title' : title,
                 'products': 'products'})
