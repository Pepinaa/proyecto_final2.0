from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.utils import timezone
from django.conf import settings

'''class Post(models.Model):
    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(max_length=250)
    quote = models.TextField()
    link = models.URLField(null=True, blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='images/default.png'
    )
    published = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='network_user_post'
    )
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.quote'''

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts', null=True)
    image = models.ImageField(null=True)
    likes = models.PositiveIntegerField(default=0, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quote = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.quote

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments', null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)
    text = models.TextField()
