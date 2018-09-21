from django import forms
from .models import Department, Driver

class DriverEditForm(forms.ModelForm):
    """
    驾驶员表单
    """
    class Meta:
        model = Driver
        fields = ('name', 'work_number', 'car_number', 'tel', 'scheduling', 'place', 'department')
        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'work_number': forms.TextInput(attrs={'class': 'form-control'}),
            'car_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tel': forms.TextInput(attrs={'class': 'form-control'}),
            'scheduling': forms.Select(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }