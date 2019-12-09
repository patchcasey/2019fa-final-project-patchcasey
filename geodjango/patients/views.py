from django.shortcuts import render
from django.views.generic import DetailView
from .models import Patient


class PatientDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'patients/patient-detail.html'
    model = Patient

# Create your views here.
