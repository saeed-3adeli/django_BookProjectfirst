from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.form import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser


# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )
    list_display = ('username', 'email', 'is_staff', 'age', 'is_active')


admin.site.register(CustomUser, CustomUserAdmin)
