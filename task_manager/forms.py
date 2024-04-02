from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                               'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
