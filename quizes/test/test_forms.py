from django.test import TestCase
from django.urls import resolve

from quizes.forms import QuizForm
from quizes.models import Quiz


class QuizFormTest(TestCase):

    def test_form_renders_item_text_input(self):
        form = QuizForm()
        # self.fail(form.as_p())


