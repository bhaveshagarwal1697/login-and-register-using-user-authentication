from django.contrib import admin

# Register your models here.

from .models import LoginModel

admin.site.register(LoginModel)
