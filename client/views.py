from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser, ClientLogin

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.isClient() and (not ClientLogin.objects.filter(clientUser=user.id)):
                return render(request, 'login.html', {'error': 'Not authorized'})
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('/users/login/')