from django.test import TestCase, SimpleTestCase
from django.urls import resolve
from http import HTTPStatus

from django.utils.html import escape

from accounts.views import register


class RegisterViewTests(TestCase):

    def test_register_url_resolves_to_register_view(self):
        found = resolve('/account/register')
        self.assertEqual(found.func, register)

