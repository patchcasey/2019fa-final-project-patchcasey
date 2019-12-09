from django.contrib.gis.db import models
from django.contrib.gis.geos import Point



class Patient(models.Model):
    u_id = models.IntegerField(unique=True)
    geom = models.PointField(default='POINT(0.0 0.0)')

    class Meta:
        # order of drop-down list items
        ordering = ('u_id',)

        # plural form in admin view
        verbose_name_plural = 'patients'