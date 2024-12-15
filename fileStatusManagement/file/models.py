from django.db import models
from client.models import Client, CustomUser

class Status(models.Model):
    COLORS_CHOICES = [
        ('success', 'success'),
        ('primary', 'primary'),
        ('warning', 'warning'),
        ('danger', 'danger'),
    ]
    title = models.CharField(max_length=500, unique=True)
    color = models.CharField(max_length=20, choices=COLORS_CHOICES)
    
    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=100)
    customerId = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name + '-' + self.customerId

class File(models.Model):
    name = models.CharField(max_length=100, unique=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class FileStatus(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    comments = models.CharField(max_length=500)
    date = models.DateField()
    drafterBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    isDraft = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('customer', 'file', 'date')