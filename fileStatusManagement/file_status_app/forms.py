from django import forms
from .models import CustomUser, FileStatus, Customer, File

class FileStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = FileStatus
        fields = ['status', 'date']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'customerId']

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'fileId', 'customer']
