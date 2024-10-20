from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomerSignUpForm, ManagerSignUpForm
from .models import CustomUser

def customer_signup(request):
    if request.method == 'POST':
        form = CustomerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_customer = True
            user.save()
            login(request, user)
            return redirect('customer_home')
    else:
        form = CustomerSignUpForm()
    return render(request, 'signup.html', {'form': form})

def manager_signup(request):
    if request.method == 'POST':
        form = ManagerSignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_manager = True
            user.save()
            login(request, user)
            return redirect('manager_home')
    else:
        form = ManagerSignUpForm()
    return render(request, 'signup.html', {'form': form})
