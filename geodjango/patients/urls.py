# from django.conf.urls import url
# from . import views
#
# app_name = 'cities'
#
# urlpatterns = [
#     url(r'^patient/(?P<pk>[0-9]+)$', views.PatientDetailView.as_view(), name='data'),
# ]

from .models import Patient
from django.views.generic import TemplateView
from django.urls import path
from django.conf.urls import url
from . import views


# urlpatterns = [
#     url(r'^$', TemplateView.as_view(template_name='patients/index.html'), name='index')
# ]

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index')
    ]