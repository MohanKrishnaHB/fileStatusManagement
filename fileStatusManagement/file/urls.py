from django.urls import path
from .views import dashboard, status, get_customers, get_file_status, upsert_file_status

app_name = 'file'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('status/', status, name='status'),
    path('get-customers/', get_customers, name='get_customers'),
    path('get-file-status/', get_file_status, name='get_file_status'),
    path('upsert-file-status/', upsert_file_status, name='upsert_file_status'),
]