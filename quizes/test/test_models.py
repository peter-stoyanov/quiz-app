from django.test import TestCase
from django.urls import resolve

from quizes.models import Quiz
from quizes.views import view_quiz, create_quiz

# helpers
def create_quiz(title):
    quiz = Quiz()
    quiz.title = title
    quiz.full_clean()
    quiz.save()
    return quiz


class QuizModelTest(TestCase):

    # purely integration test ?
    # TODO: what is expected to fail here, whats the point ?
    def test_quiz_save_and_retrieve(self):
        create_quiz('Hard quiz')

        quizes = Quiz.objects.all()
        self.assertEqual(quizes.count(), 1)
        saved_quiz = quizes[0]
        self.assertEqual(saved_quiz.title, 'Hard quiz')

    def test_quiz_has_persisted_uuid(self):
        create_quiz('Hard quiz')

        quizes = Quiz.objects.all()
        saved_quiz = quizes[0]
        self.assertTrue(saved_quiz.uuid, 'Missing uuid')

        quizes2 = Quiz.objects.all()
        saved_quiz2 = quizes2[0]

        self.assertEqual(saved_quiz.uuid, saved_quiz2.uuid, 'UUID is new each time instead of persisted')

    def test_quiz_title_max_length(self):
        create_quiz('This is intentionally looooooooooooooooooooong string')
        # self.assertRaises()
