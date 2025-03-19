from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class RegisterForm(forms.ModelForm):
    
    password = forms.CharField(widget=(forms.PasswordInput(attrs={'type':'password', 'class':'form-control'})))
    confirm_password = forms.CharField(widget=(forms.PasswordInput(attrs={'type':'password', 'class':'form-control last'})))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_image', 'password', 'confirm_password']
        widgets = {
            'email':forms.EmailInput({'type':'email', 'class':'form-control'}),
            'username':forms.TextInput({'type':'text', 'class':'form-control'}),
            'profile_image':forms.ClearableFileInput({'class':'control'}),
        }
        labels = {
            'email':'Email Address',
        }

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
