from django import forms
from django.forms import inlineformset_factory
from django.forms import BaseInlineFormSet
from .models import *


QuestionFormSet = inlineformset_factory(Question, Answer, fields='question')


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']


class AnswerForm(forms.ModelForm, BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['question'] = QuestionFormSet

    class Meta:
        model = Answer
        fields = ['text', 'question', 'author']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
