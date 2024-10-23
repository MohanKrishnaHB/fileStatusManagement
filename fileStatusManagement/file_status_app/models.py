from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_manager = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_viewer = models.BooleanField(default=False)

class Customer(models.Model):
    name = models.CharField(max_length=100)
    customerId = models.CharField(max_length=100, unique=True)

class File(models.Model):
    name = models.CharField(max_length=100)
    fileId = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class FileStatus(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('not_available', 'Not Available'),
        ('processed', 'Processed'),
        ('not_validated', 'Not Validated'),
    ]
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comments = models.CharField(max_length=500)
    date = models.DateField()
    updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    draft = models.BooleanField(default=True)
