from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from .models import Profile


class LoginForm(forms.Form):
    """登录表单"""
    username = forms.CharField(label='用户名', help_text='用户名', widget=forms.TextInput(attrs=({'class': 'form-control', 'placeholder':'用户名'})))
    password = forms.CharField(label='密码', widget=forms.TextInput(attrs=({'class':'form-control', 'type': 'password', 'placeholder':'密码'})))
    captcha = CaptchaField()


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'department', 'cpt_add', 'cpt_delete', 'cpt_edit', 'driver_add', 'driver_delete', 'driver_edit')
        wigets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
            'cpt_add': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'cpt_edit': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'cpt_delete': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_add': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_edit': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_delete': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
        }

class UserRegistrationForm(forms.ModelForm):
    """用户注册表单"""
    password = forms.CharField(label='密码', widget=forms.TextInput(attrs=({'class':'form-control', 'type':'password', 'placeholder':'密码'})))
    re_password = forms.CharField(label='密码', widget=forms.TextInput(attrs=({'class':'form-control', 'type':'password', 'placeholder':'密码'})))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')
        # 样式配置
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '名字'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '邮箱地址'}),
        }

    def clean_re_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['re_password']:
            raise forms.ValidationError('两次密码输入错误！')
        return cd['re_password']

class ProfileRegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('department', 'cpt_add', 'cpt_delete', 'cpt_edit', 'driver_add', 'driver_delete', 'driver_edit','user')
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'cpt_add': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'cpt_edit': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'cpt_delete': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_add': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_edit': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'driver_delete': forms.CheckboxInput(attrs={'class': 'checkbox form-control iCheck'}),
            'user': forms.Select(attrs={'class': 'form-control'}),
        }