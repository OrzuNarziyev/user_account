from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


# Register your models here.

class CustoUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['id', 'image', 'email', 'username', 'first_name', 'last_name', 'is_staff', ]


admin.site.register(CustomUser, CustoUserAdmin)
