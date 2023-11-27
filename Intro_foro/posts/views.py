from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import HttpResponseRedirect

@login_required

def like_post(request, pk):
    post = Post.objects.get(pk=pk)
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    liked_posts = Post.objects.filter(likes=request.user)
    return render(request, 'posts/posts.html', {'posts': posts, 'liked_posts': liked_posts})


def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  
            post.save()
            return redirect('posts:posts')


    return render(request, 'posts/create_post.html', {'form': form})


def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if post.author != request.user:
        raise Http404("No tienes permiso para editar este post")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("posts:posts")

    return render(request, 'posts/create_post.html', {'form': form})


def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if post.author != request.user:
        raise Http404("No tienes permiso para eliminar este post")

    if request.method == "POST":
        post.delete()
        return redirect("posts:posts")

    return render(request, 'posts/delete_post.html', {'post': post})