from django import forms
from .models import PostM, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Введіть ім'я"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "Введіть пароль"}))
    class Meta:
        model = User
        fields = ['username','password']

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']