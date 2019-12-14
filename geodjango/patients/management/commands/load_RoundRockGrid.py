import os
import json
import pandas as pd
from django.db import transaction
from django.core.management import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import fromstr
from django.contrib.gis.utils import LayerMapping
from ...models import RoundRockGrid

class Command(BaseCommand):
    help = "Loads grid to db"

    def handle(self, *args, **options):
        RoundRockGrid.objects.all().delete()
        # adapted from https://gis.stackexchange.com/questions/311970/load-multipolygons-from-geojson-into-geodjango-model
        filename = "grid (1).shp"
        roundrockgrid_grid = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", 'data', 'RoundRockGrid', filename),
        )

        mapping = {'name': 'FID',  # The 'name' model field maps to the 'FID' layer field.
                   'mpoly': 'POLYGON',  # For geometry fields use OGC name.
                   }

        lm = LayerMapping(RoundRockGrid, roundrockgrid_grid, mapping)
        lm.save(verbose=True)
