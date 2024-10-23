from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES_CHOICES = [
        ('champ', 'Champ'),
        ('lead', 'Lead'),
        ('client', 'Client'),
    ]
    role = models.CharField(max_length=20, choices=ROLES_CHOICES)

    def __str__(self):
        return self.email

class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class ClientLogin(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    clientUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=True)
    
    def __str__(self):
        return self.client + ' | ' + self.clientUser