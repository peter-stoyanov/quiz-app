import uuid

from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase
from django.urls import resolve
from http import HTTPStatus

from accounts.views import register, login, logout


class RegisterViewTests(TestCase):

    def test_register_url_resolves_to_register_view(self):
        found = resolve('/account/register')
        self.assertEqual(found.func, register)

    def test_for_correct_template(self):
        response = self.client.get('/account/register')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Register')
        self.assertTemplateUsed(response, 'register.html')

    def test_for_correct_form_instance(self):
        response = self.client.get('/account/register')
        self.assertIsInstance(response.context['form'], UserCreationForm)

    def test_valid_post_should_create_user(self):
        # Note: move to reusable helper/util class
        username = uuid.uuid4().hex[:8].upper()
        password = uuid.uuid4().hex[:8].upper()
        form = {'username': username, 'password1': password, 'password2': password}

        response = self.client.post('/account/register', data=form)

        user = User.objects.get(username=username)
        self.assertIsNotNone(user)
        self.assertRedirects(response, '/account/login')

    def test_invalid_post_should_return_errors(self):
        form = {'username': 'test'}
        response = self.client.post('/account/register', data=form)
        self.assertTemplateUsed(response, 'register.html')
        self.assertContains(response, 'This field is required')


class LoginViewTests(TestCase):
    fixtures = ['test_user.json']

    def test_login_url_resolves_to_login_view(self):
        found = resolve('/account/login')
        self.assertEqual(found.func, login)

    def test_for_correct_template(self):
        response = self.client.get('/account/login')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Login')
        self.assertTemplateUsed(response, 'login.html')

    def test_for_correct_form_instance(self):
        response = self.client.get('/account/login')
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_valid_post_should_login_user(self):
        form = {'username': 'test_user', 'password': 'test123456'}
        response = self.client.post('/account/login', data=form)
        user = auth.get_user(self.client)

        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, '/')

    def test_invalid_post_should_return_errors(self):
        form = {'username': 'no_such_user', 'password': 'fake'}
        response = self.client.post('/account/login', data=form)
        self.assertTemplateUsed(response, 'login.html')
        self.assertContains(response, 'Please enter a correct username and password')


class LogoutViewTests(TestCase):

    def test_logout_url_resolves_to_logout_view(self):
        found = resolve('/account/logout')
        self.assertEqual(found.func, logout)

    def test_valid_post_should_login_user(self):
        user = User.objects.create_user(username='testuser', password='12345678')
        self.client.login(username=user.username, password='12345678')

        response = self.client.post('/account/logout')

        user = auth.get_user(self.client)
        self.assertIsInstance(user, AnonymousUser)
        self.assertRedirects(response, '/')
