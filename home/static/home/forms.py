from django import forms
# INHALT
# - eigene forms zB für die Registrierung erstellen.

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label='Username')
    email_address = forms.EmailField(label='Email Address')
    password = forms.CharField(min_length=8, max_length=30, label='Password', widget=forms.PasswordInput)
