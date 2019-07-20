from django.shortcuts import render

def signup(request):
    return render(request, 'accounts/signup.html')

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    #TODO: need to route to homepage
    #and logout
    return render(request, 'accounts/logout.html')

