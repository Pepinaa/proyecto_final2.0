from django.urls import path
from .views import change_profile_picture
from . import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/<slug:slug>', views.user_detail, name='user_detail'),
    path("follow/<slug:slug>", views.follow, name='follow'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
]
