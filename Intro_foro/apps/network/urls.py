from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'network'

urlpatterns = [
    path('home', views.casa, name='casa'),
]