from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'department', 'cpt_add', 'cpt_delete', 'cpt_edit', 'driver_add', 'driver_delete', 'driver_edit')
	search_fields = ('user',)
	