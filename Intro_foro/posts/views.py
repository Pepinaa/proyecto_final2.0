from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment

def posts(request):
    post = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts.html', {'posts': posts})
