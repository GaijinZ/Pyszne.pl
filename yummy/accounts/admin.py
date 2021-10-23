from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import RegisterForm


class UsersAdmin(UserAdmin):
    add_form = RegisterForm

    list_display = ('email', 'last_name', 'is_superuser')
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_superuser', 'is_active')}),
        ('User info', {'fields': ('id', 'date_joined', 'last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('id', 'date_joined', 'last_login',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UsersAdmin)
