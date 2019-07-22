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

@login_required
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and rrequest.POST['url'] and request.POST['icon'] and request.POST['image']:
        else:
            return render(request, 'products/create.html', 
                          {'error': 'All fields are required.'}) 
    else:
        return render(request, 'products/create.html')
