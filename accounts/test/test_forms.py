import uuid

from django.test import TestCase

from accounts.forms import RegisterForm


class RegisterFormTest(TestCase):

    def test_for_blank_username(self):
        form = RegisterForm(data={'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['username'],
            ["This field is required."]
        )

    def test_for_long_username(self):
        form = RegisterForm(data={'username': "x" * 151})
        self.assertFalse(form.is_valid())
        self.assertTrue("Ensure this value has at most 150 characters" in str(form.errors['username']))

    def test_for_unique_username(self):
        username = uuid.uuid4().hex[:8].upper()
        password = uuid.uuid4().hex[:8].upper()
        register_user_form = RegisterForm(data={'username': username, 'password': password})
        register_user_form.save()

        form = RegisterForm(data={'username': username})

        self.assertFalse(form.is_valid())
        self.assertTrue("A user with that username already exists" in str(form.errors['username']))

    def test_for_long_first_name(self):
        form = RegisterForm(data={'first_name': "x" * 151})
        self.assertFalse(form.is_valid())
        self.assertTrue("Ensure this value has at most 150 characters" in str(form.errors['first_name']))

    def test_for_long_last_name(self):
        form = RegisterForm(data={'last_name': "x" * 151})
        self.assertFalse(form.is_valid())
        self.assertTrue("Ensure this value has at most 150 characters" in str(form.errors['last_name']))

