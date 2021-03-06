from django import forms
from .models import *


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'title': forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
        }


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }


