from django.urls import path
from .views import file_status_manager_view, file_status_admin_view, file_status_viewer_view

urlpatterns = [
    path('manager/', file_status_manager_view, name='file_status_manager_view'),
    path('admin/', file_status_admin_view, name='file_status_admin_view'),
    path('viewer/', file_status_viewer_view, name='file_status_viewer_view'),
]
