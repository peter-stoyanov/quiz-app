from django.test import TestCase

# Create your tests here.
from django.urls import resolve
from .views import quiz_page


class QuizPageTest(TestCase):

    def test_guid_link_resolves_to_quiz_page_view(self):
        found = resolve('/quiz/asd1289jaS')
        self.assertEqual(found.func, quiz_page)
