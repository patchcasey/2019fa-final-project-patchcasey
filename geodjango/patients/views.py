from django.shortcuts import render
import os
from json import dumps
import shapefile
from django.views.generic import DetailView
from .models import Patient, AustinGrid, RoundRockGrid


def index(request):
    roundrock_objects = RoundRockGrid.objects.all()
    patient_objects = Patient.objects.all()
    austingrid_objects = AustinGrid.objects.all()

    roundrockgrid_grid_shapefile = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'data', "RoundRockGrid", "grid (1)"),
    )

    # serializer adapted from https://stackoverflow.com/questions/43119040/shapefile-into-geojson-conversion-python-3
    # the intent of this was to expose the grid in a way that Leaflet could read, but it did not work

    reader = shapefile.Reader(roundrockgrid_grid_shapefile)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", \
                           geometry=geom, properties=atr))

        # write the GeoJSON file

    roundrock_geojson = dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n"

    context = {'roundrock': roundrock_geojson,
               'patient': patient_objects,
               'austin':austingrid_objects}

    return render(request, "patients/index.html", context)

# Create your views here.
