from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User  # Импортируем модель User
from django import forms


# class LoginForm(AuthenticationForm):
#     username = forms.CharField(
#         label='Ваш логин',
#         widget=forms.TextInput(attrs={'class': 'form-control', }),
#         min_length=2,
#     )
#     password = forms.CharField(
#         label='Ваш пароль',
#         widget=forms.PasswordInput(attrs={'class': 'form-control', }),
#     )