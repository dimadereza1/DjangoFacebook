from django import forms
from .models import PostM, New_user
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import datetime

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введіть ім'я"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введіть пароль"}))
    class Meta:
        model = New_user
        fields = ['username','password']

class RegisterForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введіть пошту", 'class':'reg_forms_r'}))
    passwordd = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введіть пароль", 'class':'reg_forms_r'}))
    class Meta:
        model = New_user
        fields = ['email', 'passwordd']

