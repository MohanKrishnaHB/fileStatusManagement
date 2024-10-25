from django.urls import path
from .views import dashboard, status

app_name = 'file'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('status/', status, name='status'),
]