from django import forms
from .models import *


class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text', 'author']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'author')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

# class AnswerForm(forms.Form):
#     parent_comment = forms.IntegerField(
#         widget=forms.HiddenInput,
#         required=False
#     )
#
#     text = forms.CharField(
#         label="",
#         widget=forms.Textarea
#     )
