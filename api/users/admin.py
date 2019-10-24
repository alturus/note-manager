from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import gettext_lazy as _

from api.users.models import User


class UserAdmin(DjangoUserAdmin):
    ordering = ('username',)
    readonly_fields = ('last_login', 'date_joined')
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_admin', 'is_staff')
    list_filter = ('is_admin', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_admin', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(User, UserAdmin)
