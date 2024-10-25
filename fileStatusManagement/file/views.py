from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

@login_required
def dashboard(request):
    user = request.user
    if user.isChamp():
        return render(request, 'champ/dashboard.html')
    elif user.isClient():
        return render(request, 'client/dashboard.html')
    else:
        logout(request)
        return render(request, 'login.html', {'error': 'Access Denied'})
