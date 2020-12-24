import json

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
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


def add_to_session(request):
    request.session['likes'] = 9
    return HttpResponse('added')


def session(request):
    from django.contrib.sessions.models import Session
    from django.contrib.auth.models import User

    # session_key = '8cae76c505f15432b48c8292a7dd0e54'
    #
    # session = Session.objects.get(session_key=session_key)
    session_data = request.session
    uid = session_data.get('_auth_user_id', 'no user id found in session')
    # print(uid)
    #
    # print
    # user.username, user.get_full_name(), user.email
    # serialized = dict((key, value) for key, value in session_data.__dict__
    #                   if not callable(value) and not key.startswith('__'))
    return HttpResponse(json.dumps(session_data.__dict__['_session_cache']))
