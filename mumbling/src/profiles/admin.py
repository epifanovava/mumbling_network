from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from .models import UserNet
from django.contrib.auth.admin import UserAdmin


class UserNetAdmin(UserAdmin):
    list_display = ('username', 'email', 'phone', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'middle_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Info'), {'fields': ('phone', 'avatar', 'gender')}),
    )


admin.site.register(UserNet, UserNetAdmin)
