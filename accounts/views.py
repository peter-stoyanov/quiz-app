from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
from accounts.forms import RegisterForm


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
