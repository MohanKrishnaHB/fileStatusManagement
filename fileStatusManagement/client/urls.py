from django.urls import path
from .views import get_login

urlpatterns = [
    path('login/', get_login, name='get_login'),
]