from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_question')
    likes = models.ManyToManyField(User, related_name='likes_question')
    objects = QuestionManager()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    question = models.ForeignKey(Question, related_name='text_question')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_answer')
