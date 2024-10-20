from django.urls import path
from . import views

urlpatterns = [
    path('signup/customer/', views.customer_signup, name='customer_signup'),
    path('signup/manager/', views.manager_signup, name='manager_signup'),
]
