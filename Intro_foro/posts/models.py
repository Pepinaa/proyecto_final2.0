from django.db import models

class Post(models.Model):
    #imagen = models.ImageField()
    likes = models.PositiveIntegerField(default=0, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)

class Comment(models.Model):
    text = models.TextField()
