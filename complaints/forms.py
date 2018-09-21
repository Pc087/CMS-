from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('title','complaint_number','category','record_date','happen_date','complainant','tel','content','feedback_content','is_finished','driver_name','driver_tel','driver_work_number', 'user', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'complaint_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(attrs={
                'class': 'form-control',
            }),
            'record_date': forms.DateTimeInput(attrs={
                'class': 'form_datetime form-control',
            }),
            'happen_date': forms.DateTimeInput(attrs={
                'class': 'form_datetime form-control',
            }),
            'complainant': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'tel': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'is_finished': forms.CheckboxInput(attrs={
                'class': 'checkbox form-control iCheck',
            }),
            'driver_name': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'driver_work_number': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'driver_tel': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'user': forms.Select(attrs={
                'class': 'form-control',
            }),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'feedback_content': forms.Textarea(attrs={'class': 'form-control'})
        }