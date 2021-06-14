from django.contrib import admin

from .models import Manager, State, City, Festival, Users


admin.site.register(Manager)
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
    
