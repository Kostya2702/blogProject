from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-id')

    def popular(self):
        return self.order_by('-rating')


class Question(models.Model):
    objects = QuestionManager()
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    likes = models.ManyToManyField(User, related_name='likes_question', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('question', kwargs={'quest_id': self.pk})


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, related_name='question')
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        ordering = [
            '-added_at'
        ]
