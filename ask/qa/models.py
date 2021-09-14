from django.contrib.auth.models import User
from django.db import models


class QuestionManager(models.Manager):
    def new(self):
        return super().get_queryset().order_by('-added_at_q')

    def popular(self):
        return super().get_queryset().order_by('-likes')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_question')
    likes = models.ManyToManyField(User,
                                   related_name='likes_question')

    objects = models.Manager()
    question_text = QuestionManager()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now=True)
    question = models.ManyToManyField(User,
                                      related_name='likes_answer')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='author_answer')
