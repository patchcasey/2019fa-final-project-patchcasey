import os
import pandas as pd
from django.core.management import BaseCommand
from ...models import Patient, AustinGrid

def totally_real_regression_equation(*args):
    pass

class Command(BaseCommand):
    help = "performs spatial lookup"
    def handle(self, *args, **options):

        intersects = {}

        for patient in Patient.objects.all():
            # this finds the FID of the part of the grid the point exists in
            # this would be to find what underlying demographics of the region
            # influence patients coming from this location
            geom = patient.geom
            intersect_grid_lookup = AustinGrid.objects.get(mpoly__intersects=geom)
            intersect_grid_id = int((str(intersect_grid_lookup).split()[1]))
            intersects.update({patient.pk:intersect_grid_id})

        # This section simulates a logistic regressions
        # obviously with this dummy data, we would not get any correlation
        # but this is not a data science class, it is a Python class!
        # for that reason, I am using a garbage "model" to show how it could be applied
        totally_real_regression_equation(intersects)

        #outputs from coefficient
        output_coefficient1 = -456.628
        output_coefficient2 = 2.383










