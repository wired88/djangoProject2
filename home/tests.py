from django.test import TestCase

# Create your tests here.
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

class RegisterView(View):
    def get(self, request):
        register_form = UserCreationForm()
        return render(request, 'home/register.html', {'register_form': register_form})

    def post(self, request):
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            username = register_form.cleaned_data.get('username')
            password = register_form.cleaned_data.get('password1')
            if user := authenticate(request, username=username, password=password):
                login(request, user)
                return redirect(reverse('home:index'))
            else:
                messages.error(request, 'Invalid E-Mail or Password')
        return render(request, 'home/register.html', {'register_form': register_form})