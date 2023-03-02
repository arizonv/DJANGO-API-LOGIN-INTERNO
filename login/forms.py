from datetime import datetime
from django import forms
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
import requests


class AuthenticationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese un username',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese un password',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def get_or_create_user_api(self, username, password):
        response = {'resp': False, 'msg': 'No se ha podido iniciar sesión'}
        try:
            payload = {
                'username': username,
                'password': password,
            }
            r = requests.post('http://127.0.0.1:8000/api/login/', data=payload)
            if r.status_code == 200:
                response = r.json()
            else:
                response['msg'] = r.text
        except Exception as e:
            response = {'resp': False, 'msg': str(e)}
        return response

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get('username', '')
        password = cleaned.get('password', '')
        if len(username) == 0:
            raise forms.ValidationError('Ingrese su username')
        elif len(password) == 0:
            raise forms.ValidationError('Ingrese su password')
        return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)
