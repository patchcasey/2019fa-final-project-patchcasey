from django.contrib.gis import admin
from .models import Patient
from leaflet.admin import LeafletGeoAdmin

# admin.site.register(Patient, admin.GeoModelAdmin)

class PatientAdmin(LeafletGeoAdmin):
    list_display = ('u_id', 'geom')

admin.site.register(Patient, PatientAdmin)