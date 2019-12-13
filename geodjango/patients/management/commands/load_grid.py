import os
import json
import pandas as pd
from django.db import transaction
from django.core.management import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import fromstr
from django.contrib.gis.utils import LayerMapping
from ...models import AustinGrid

class Command(BaseCommand):
    help = "Loads grid to db"

    def handle(self, *args, **options):
        # adapted from https://gis.stackexchange.com/questions/311970/load-multipolygons-from-geojson-into-geodjango-model
        filename = "grid - Copy.shp"
        austin_grid = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", 'data', 'grid', filename),
        )

        mapping = {'name': 'FID',  # The 'name' model field maps to the 'FID' layer field.
                   'mpoly': 'POLYGON',  # For geometry fields use OGC name.
                   }

        lm = LayerMapping(AustinGrid, austin_grid, mapping)
        lm.save(verbose=True)

        # with open(austin_grid) as fd:
        #     # data = json.load(fd)
        #     # for feature in data['features']:
        #     #     if feature['geometry']['type']:
        #     #         feature['geometry']['type'] = 'MultiPolygon'
        #     #         feature['geometry']['coordinates'] = [feature['geometry']['coordinates']]
        #     #
        #     #     geom = GEOSGeometry(str(feature['geometry']))
        #     #
        #     #
        #     #     grid_model = Grid(
        #     #         geom=GEOSGeometry(geom)
        #     #     )
        #     #     grid_model.save()
