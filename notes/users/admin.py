from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

    
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    
    list_display = ('email', 'first_name','last_name','is_staff', 'is_active',)
    list_filter = ('email', 'first_name','last_name', 'is_staff', 'is_active',)
    
    fieldsets = (
        (None, {'fields': ('email' ,'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
        ('Important dates', {'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email' ,'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    search_fields = ('email','first_name', 'last_name')
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)