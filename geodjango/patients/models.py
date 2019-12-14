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

class AustinGrid(models.Model):
    name = models.IntegerField(default=0)
    mpoly = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return 'Name: {}'.format(self.name)

class RoundRockGrid(models.Model):
    name = models.IntegerField(default=0)
    mpoly = models.MultiPolygonField(srid=4326)
    color = models.FloatField(default=0)

    def __str__(self):
        return 'Name: {}'.format(self.name)

