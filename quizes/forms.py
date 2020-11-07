from django import forms

from quizes.models import Quiz


class QuizForm(forms.Form):
    title = forms.CharField()

    class Meta:
        model = Quiz
        fields = ('title',)


