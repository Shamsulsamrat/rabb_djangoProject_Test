# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email','password1','password2')
        widgets = {
            'first_name': forms.TextInput(
                attrs={'placeholder': 'First Name', 'style': 'width: 300px;', 'class': 'form-control'}),
            'last_name': forms.TextInput(
                attrs={'placeholder': 'Last Name', 'style': 'width: 300px;', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email', 'style': 'width: 300px;', 'class': 'form-control'}),
            'password1': forms.PasswordInput(
                attrs={'placeholder': 'Password', 'style': 'width: 300px;', 'class': 'form-control'}),
            'password2': forms.PasswordInput(
                attrs={'placeholder': 'CPassword', 'style': 'width: 300px;', 'class': 'form-control'}),

        }
