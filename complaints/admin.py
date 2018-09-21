from django.contrib import admin
from .models import Complaint

# Register your models here.

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'record_date', 'happen_date', 'complaint_number')
    list_editable = ('category',)
    search_fields = ('title', 'record_date', 'happen_date')
    list_filter = ('title', 'record_date', 'happen_date', 'category')
    list_per_page = 10

    class Media:
	      js = (
	      		"/static/js/editor/ckeditor.js",
	          "/static/js/editor/config.js",
	      )
		