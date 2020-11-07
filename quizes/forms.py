from django import forms

from quizes.models import Quiz


class QuizForm(forms.models.ModelForm):

    class Meta:
        model = Quiz
        fields = ('title',)
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a quiz title',
                'class': 'quiz-title-input',
            }),
        }
        error_messages = {
            'title': {
                'required': "You can't have a quiz with empty title",
                'max_length': "You can't have a quiz with more than 40 characters"
            }
        }


