from django.urls import path
from .views import dashboard

app_name = 'file'

urlpatterns = [
    path('', dashboard, name='dashboard'),
]