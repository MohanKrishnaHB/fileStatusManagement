from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from client.models import Client
from .models import Customer, File, FileStatus, Status
from datetime import date

@login_required
def dashboard(request):
    user = request.user
    if user.isChamp():
        return render(request, 'champ/dashboard.html')
    elif user.isClient():
        return render(request, 'client/dashboard.html')
    else:
        logout(request)
        return redirect('/admin')

@login_required
def status(request):
    user = request.user
    if user.isChamp():
        clients = Client.objects.all()
        customers = Customer.objects.filter(client=clients[0].id).values()
        files = File.objects.filter(client=clients[0].id).values()
        status = Status.objects.all()
        retrunObj = {
            'clients': clients,
            'customers': customers,
            'files': files,
            'status': status,
            'date': date.today().strftime("%Y-%m-%d")
        }
        return render(request, 'champ/status.html', retrunObj)
    elif user.isClient():
        return render(request, 'client/status.html')
    else:
        logout(request)
        return redirect('/admin')
