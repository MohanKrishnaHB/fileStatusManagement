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

    def isChamp(self):
        return self.role == 'champ'
    def isClient(self):
        return self.role == 'client'
    def isLead(self):
        return self.role == 'lead'

class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class ClientLogin(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    clientUser = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.client + ' | ' + self.clientUser