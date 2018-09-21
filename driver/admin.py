from django.contrib import admin
from .models import Driver, Department

# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'work_number', 'car_number', 'department', 'scheduling', 'place')
    search_fields = ('name', 'work_number', 'car_number', 'department')
    list_filter= ('department',)
    list_per_page = 20


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
