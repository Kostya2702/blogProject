from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Ip(models.Model):
    ip = models.CharField(max_length=10)

    def __str__(self):
        return self.ip


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-views')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now=True)
    views = models.ManyToManyField(Ip, related_name='views', blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', kwargs={'quest_id': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(blank=True, auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='question')
    author = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        ordering = [
            '-added_at'
        ]
