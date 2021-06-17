from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import City, Festival, Manager, State, Users


class UserAdminConfig(UserAdmin):
    ordering = ('user_name', )
    list_display = ('email', 'user_name', 'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'user_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )

admin.site.register(Manager, UserAdminConfig)

admin.site.register(State)
admin.site.register(City)

@admin.register(Festival)
class FestivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'start_date', 'finish_date', 'country', 'city']
    list_filter = ['city', 'country']
    prepopulated_fields = {'slug': ('name',)}




@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'festival']
    list_filter = ['email', 'festival']
    

