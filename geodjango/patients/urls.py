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
from djgeojson.views import GeoJSONLayerView
from django.conf.urls import url


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    url(r'^patient.geojson$', GeoJSONLayerView.as_view(model=Patient), name='data')
]