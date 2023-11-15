from django.urls import path
from django.views.generic import TemplateView
from . import views
app_name = 'network'

urlpatterns = [
    path('alo', views.casa, name='casa'),
]