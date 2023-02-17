from django.contrib import admin
from .models import User
from account.models.company import Company
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = User
    list_display= ('email','is_superuser','is_active','is_verified')
    list_filter = ('email','is_superuser','is_active','is_verified','the_employer','employee','company')
    search_fields=('email',)
    ordering = ('email',)
    fieldsets = (
        ('Authentications', {
            "fields": (
                'email','password'
            ),
        }),
        ('permissions',
        {
            "fields":(
                'is_staff','is_active','is_superuser','is_verified','the_employer','employee','company'
            )
        }),
        ('group permissions',
        {
            "fields":(
                'groups','user_permissions'
            )
        }),
        ('date',
        {
            "fields":(
               'last_login',
            )
        }),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2","is_staff",'is_active','is_superuser','is_verified','the_employer','employee','company'),
            },
        ),
    )

admin.site.register(User,CustomUserAdmin)

admin.site.register(Company)
