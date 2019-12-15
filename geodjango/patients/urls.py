from .models import Patient
from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index')
    ]