from django.shortcuts import render
from .models import Post

def casa(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'posts': data})