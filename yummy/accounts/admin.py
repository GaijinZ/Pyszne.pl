from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User
from .forms import RegisterForm


class UsersAdmin(UserAdmin):
    add_form = RegisterForm

    list_display = ('email', 'is_superuser')
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UsersAdmin)
