from django.urls import path, re_path
from django.views.generic.base import TemplateView

from . import views

app_name = 'public'

urlpatterns = [
	path('index', views.index, name='index'),
    path('', views.mainPage, name='mainPage'),
]