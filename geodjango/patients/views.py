from django.shortcuts import render
from django.views.generic import DetailView
from .models import Patient, AustinGrid, RoundRockGrid


def index(request):
    roundrock_objects = RoundRockGrid.objects.all()
    patient_objects = Patient.objects.all()
    austingrid_objects = AustinGrid.objects.all()

    context = {'roundrock': roundrock_objects,
               'patient': patient_objects,
               'austin':austingrid_objects}

    return render(request, "patients/index.html", context)

# Create your views here.
