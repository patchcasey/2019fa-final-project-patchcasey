from django.contrib.gis import admin
from .models import Patient, AustinGrid
from leaflet.admin import LeafletGeoAdmin

# admin.site.register(Patient, admin.GeoModelAdmin)

class PatientAdmin(LeafletGeoAdmin):
    list_display = ('u_id', 'geom')

class AustinGridAdmin(LeafletGeoAdmin):
    list_display = ('pk', 'mpoly')

admin.site.register(Patient, PatientAdmin)
admin.site.register(AustinGrid, AustinGridAdmin)