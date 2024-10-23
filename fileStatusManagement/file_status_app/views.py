from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import FileStatusUpdateForm, CustomerForm, FileForm
from .models import FileStatus, CustomUser, Customer, File

def file_status_manager_view(request):
    if request.method == 'POST':
        form = FileStatusUpdateForm(request.POST)
        if form.is_valid():
            file_status = form.save(commit=False)
            file_status.updated_by = request.user
            file_status.save()
            return redirect('file_status_manager_view')
    else:
        form = FileStatusUpdateForm()
    return render(request, 'file_status_manager_view.html', {'form': form})

def file_status_admin_view(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        file_form = FileForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
        if file_form.is_valid():
            file_form.save()
        return redirect('file_status_admin_view')
    else:
        customer_form = CustomerForm()
        file_form = FileForm()
    return render(request, 'file_status_admin_view.html', {
        'customer_form': customer_form,
        'file_form': file_form,
    })

def file_status_viewer_view(request):
    customers = Customer.objects.filter(customuser=request.user)
    file_statuses = FileStatus.objects.filter(file__customer__in=customers)
    return render(request, 'file_status_viewer_view.html', {'file_statuses': file_statuses})
