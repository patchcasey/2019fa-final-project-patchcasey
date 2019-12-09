import os
import pandas as pd
from django.db import transaction
from django.core.management import BaseCommand
from django.contrib.gis.geos import fromstr
from ...models import Patient

class Command(BaseCommand):
    help = "Loads patients to db"

    def handle(self, *args, **options):
        #TODO - change this from hardcode
        filename = "testdata.csv"
        patient_data = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", 'data', filename),
        )

        data_mapping = {
            "u_id": "id",
            "geom": "geom"
        }

        df = pd.read_csv(patient_data)
        df["geom"] = df["lon"].map(str)+ " " + df["lat"].map(str)

        with transaction.atomic():
            patient_objs = [
                Patient(
                    u_id=value["id"],
                    geom=fromstr('POINT(' + value["geom"] + ')', srid=4326)
                )
                for key, value in df.iterrows()
            ]
            #TODO - remove this to append?
            Patient.objects.all().delete()
            Patient.objects.bulk_create(patient_objs)
