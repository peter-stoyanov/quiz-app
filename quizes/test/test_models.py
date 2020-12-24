from django.core.exceptions import ValidationError
from django.test import TestCase

from quizes.models import Quiz


class QuizModelTest(TestCase):

    # Note: what is expected to fail here, whats the point - integration test ?
    def test_quiz_save_and_retrieve(self):
        quiz = Quiz(title='Hard quiz')
        quiz.save()

        quizes = Quiz.objects.all()
        self.assertEqual(quizes.count(), 1)
        saved_quiz = quizes[0]
        self.assertEqual(saved_quiz.title, 'Hard quiz')

    def test_quiz_has_persisted_uuid(self):
        quiz = Quiz(title='Hard quiz')
        quiz.save()

        quizes = Quiz.objects.all()
        saved_quiz = quizes[0]
        self.assertTrue(saved_quiz.uuid, 'Missing uuid')

        quizes2 = Quiz.objects.all()
        saved_quiz2 = quizes2[0]

        self.assertEqual(saved_quiz.uuid, saved_quiz2.uuid, 'UUID is new each time instead of persisted')

    # Note: this was later duplicated in test_forms
    def test_quiz_title_max_length(self):
        with self.assertRaises(ValidationError):
            quiz = Quiz(title='This is intentionally looooooooooooooooooooong string')
            quiz.full_clean()
            quiz.save()

