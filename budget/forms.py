from django import forms

from budget.models import Expense


class ExpenseForm(forms.models.ModelForm):

    class Meta:
        model = Expense
        fields = ('amount', 'type')
        widgets = {
            'title': forms.fields.TextInput(attrs={
                'placeholder': 'Enter a quiz title',
                'class': 'create-quiz__title-input',
            }),
        }
        error_messages = {
            'title': {
                'required': "You can't have an expense with empty name",
                'max_length': "You can't have an expense with more than 50 characters"
            }
        }

