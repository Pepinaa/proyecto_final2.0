from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime

class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.now)

    def total(self):
        return self.option_one_count + self.option_two_count

class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} votó en la encuesta: {self.poll}'