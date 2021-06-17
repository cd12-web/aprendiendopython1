import datetime
from django.db import models
from django.utils import timezone


class Choice(models.Model):
    question = models.ForeignKey('polls.Question', on_delete=models.CASCADE,blank=True,null=True)
    choice_text = models.CharField(max_length=200,blank=True)
    votes = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.choice_text


class Question(models.Model):
    question_text = models.CharField(max_length=200,blank=True)
    pub_date = models.DateTimeField('date published',blank=True)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
