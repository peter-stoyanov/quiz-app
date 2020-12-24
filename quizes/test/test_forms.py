from django.test import SimpleTestCase

from quizes.forms import QuizForm


class QuizFormTest(SimpleTestCase):

    def test_form_validation_for_blank_quiz_title(self):
        form = QuizForm(data={'title': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            ["You can't have a quiz with empty title"]
        )

    def test_form_validation_for_too_long_quiz_title(self):
        form = QuizForm(data={'title': 'This is intentionally looooooooooooooooooooong string'})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['title'],
            ["You can't have a quiz with more than 40 characters"]
        )

    def test_form_validation_for_valid_quiz_title(self):
        form = QuizForm(data={'title': 'Some quiz title'})
        self.assertTrue(form.is_valid())


