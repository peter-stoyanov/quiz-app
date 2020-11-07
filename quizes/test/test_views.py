from django.test import TestCase
from django.urls import resolve

from quizes.models import Quiz
from quizes.views import view_quiz, create_quiz


class QuizViewTest(TestCase):

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


class CreateQuizViewTest(TestCase):

    def test_url_resolves_to_quiz_create_page_view(self):
        found = resolve('/quiz')
        self.assertEqual(found.func, create_quiz)


