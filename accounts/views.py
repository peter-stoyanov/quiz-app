from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages, auth


def register(request):
    if request.method == "POST":
        # Note: am I supposed to use these auth forms directly or subclass them?
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password')
            )
            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are now logged in')
                return redirect('/')
            else:
                messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
    return redirect('/')
