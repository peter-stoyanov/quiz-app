from django import forms
from django.core.exceptions import ValidationError


class ArticleForm(forms.Form):
    title = forms.CharField()
    pub_date = forms.DateField()

    def clean_title(self):
        value = self.cleaned_data['title']
        if 'pesho' in value:
            return value
        raise ValidationError('Title is not valid', 'special')

