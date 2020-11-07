from django.test import TestCase
from django.urls import resolve

from http import HTTPStatus

from django.utils.html import escape

from quizes.forms import QuizForm
from quizes.models import Quiz
from quizes.views import view_quiz, create_quiz, list_quizes


class QuizViewTests(TestCase):

    def test_uuid_link_resolves_to_quiz_page_view(self):
        found = resolve('/quiz/075194d3-6885-417e-a8a8-6c931e272f00')
        self.assertEqual(found.func, view_quiz)

    def test_link_with_numbers_returns_404(self):
        response = self.client.get('/quiz/075194')
        self.assertEqual(response.status_code, 404)

    def test_quiz_title_is_displayed(self):
        quiz = Quiz(title='Hard quiz')
        quiz.save()

        quizes = Quiz.objects.all()
        response = self.client.get(f'/quiz/{quiz.uuid}')
        self.assertTemplateUsed(response, 'quiz.html')
        self.assertContains(response, 'Hard quiz')


class CreateQuizViewTests(TestCase):

    def test_url_resolves_to_quiz_create_page_view(self):
        found = resolve('/quiz')
        self.assertEqual(found.func, create_quiz)

    def test_quiz_page_uses_quiz_form(self):
        response = self.client.get('/quiz')
        # Note: this assert was passing when I was not actually rendering the form in the template
        # Missing input would be caught by the functional tests though
        # should I check some html content here ?
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIsInstance(response.context['form'], QuizForm)

    def test_quiz_page_form_error(self):
        response = self.client.post('/quiz', data={'title': ''})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # all errors are contained in one property in the view
        # checking that one error is displayed should be sufficient
        self.assertContains(response, escape("You can't have a quiz with empty title"), html=True)


class QuizListViewTests(TestCase):

    def test_all_url_resolves_to_quiz_list_view(self):
        found = resolve('/quiz/all')
        self.assertEqual(found.func, list_quizes)

    def test_quiz_list_view(self):
        quiz = Quiz(title='First quiz')
        quiz.save()
        response = self.client.get('/quiz/all')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, escape('All Quizes'), html=True)
        self.assertContains(response, escape('First quiz'))
