from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirm']:
            user = User.objects.get(username=request.POST['username'])
            return render(request, 'accounts/signup.html',
                          {'error': 'Username is already in use. Please choose another.'})
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO: need to route to homepage
    #and logout
    return render(request, 'accounts/logout.html')

