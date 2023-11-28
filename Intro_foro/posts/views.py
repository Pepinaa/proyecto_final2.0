from django.shortcuts import render, redirect, get_object_or_404
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
    post_comments = {}
    for post in posts:
        comments = Comment.objects.filter(post=post)
        post_comments[post.id] = comments

    post_comments_count = {}
    for post in posts:
        post_comments_count[post.id] = post.comments.count()

    return render(request, 'posts/posts.html', {'posts': posts, 'post_comments_count': post_comments_count})

@login_required
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('posts:post-detail', pk=pk)  

    else:
        comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})