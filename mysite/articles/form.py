from cProfile import label
from dataclasses import fields
from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'imgfile']
        labels = {
            'subject' : '제목',
            'content' : '내용',
            'imgfile' : '파일',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content' : '내용'
        }