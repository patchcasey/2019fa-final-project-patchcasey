import os
import pandas as pd
from django.core.management import BaseCommand
from sklearn.ensemble import RandomForestClassifier
import shapefile
from json import dumps
from ...models import Patient, AustinGrid, RoundRockGrid

class Command(BaseCommand):
    help = "performs spatial lookup"
    def handle(self, *args, **options):

        intersects = {}
        # lookup which squares in grid have patients in them
        for patient in Patient.objects.all():
            # this finds the FID of the part of the grid the point exists in
            # this would be to find what underlying demographics of the region
            # influence patients coming from this location
            geom = patient.geom
            try:
                intersect_grid_lookup = AustinGrid.objects.get(mpoly__intersects=geom)
                intersect_grid_id = int((str(intersect_grid_lookup).split()[1]))
                intersects.update({intersect_grid_id:patient.pk})
            except:
                pass

        grid_id_names = AustinGrid.objects.all()
        grid_list = [grid.name for grid in grid_id_names]
        grid_neg_pos = []

        for x in range(210):
            if x in intersects.keys():
                grid_neg_pos.append(1)
            else:
                grid_neg_pos.append(0)

        grid_dict = {"GEO_ID":grid_list, "Patient":grid_neg_pos}

        pos_neg_df = pd.DataFrame(grid_dict)

        filename = "grid_data.csv"
        austin_grid_demog = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", 'data', filename),
        )

        roundrockgrid_grid_demog = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "..", "..", 'data', "RoundRockGrid_data.csv"),
        )


        # creates training data with demographics of each grid
        demog_df = pd.read_csv(austin_grid_demog)
        X = demog_df.drop('GEO_ID', axis=1)
        y = pos_neg_df['Patient']

        # trains random forest model
        rtree_clf = RandomForestClassifier(n_estimators=100, random_state=0, max_depth=5)
        rtree_clf.fit(X, y)

        # predicts on roundrock data set
        roundrock_demog_df = pd.read_csv(roundrockgrid_grid_demog)
        X_test = roundrock_demog_df.drop('GEO_ID', axis=1)
        probability_of_patient= list(rtree_clf.predict_proba(X_test)[:,1])

        roundrock_demog_df["patient_probability"] = probability_of_patient

        # updates roundrock data set probability of having a patient
        roundrock_model = RoundRockGrid.objects.all()
        for i in range(len(roundrock_model)):
            roundrock_model[i].color = probability_of_patient[i]
            roundrock_model[i].save()
