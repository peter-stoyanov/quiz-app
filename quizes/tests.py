from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from .views import quiz_page


class QuizPageTest(TestCase):

    def test_uuid_link_resolves_to_quiz_page_view(self):
        found = resolve('/quiz/075194d3-6885-417e-a8a8-6c931e272f00')
        self.assertEqual(found.func, quiz_page)

    def test_quiz_page_uses_quiz_template(self):
        response = self.client.get('/quiz/075194d3-6885-417e-a8a8-6c931e272f00')
        self.assertTemplateUsed(response, 'quiz.html')
