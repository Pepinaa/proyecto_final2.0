from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('create-post/', views.create_post, name='create-post'),
]