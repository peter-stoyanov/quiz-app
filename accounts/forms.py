from django import forms
from django.contrib.auth.models import User

# Notes: at some point I realised there is a built-in form for that :(
class RegisterForm(forms.models.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
        widgets = {
            'username': forms.fields.TextInput(attrs={
                'class': 'register__username-input'
            }),
            'first_name': forms.fields.TextInput(attrs={
                'class': 'register__first-name-input'
            }),
            'last_name': forms.fields.TextInput(attrs={
                'class': 'register__last-name-input'
            }),
            'email': forms.fields.TextInput(attrs={
                'class': 'register__email-input'
            }),
            'password': forms.fields.TextInput(attrs={
                'class': 'register__password-input'
            })
        }
