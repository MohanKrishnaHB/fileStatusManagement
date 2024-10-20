from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from fileStatusApp.models import *
# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(CustomUser)