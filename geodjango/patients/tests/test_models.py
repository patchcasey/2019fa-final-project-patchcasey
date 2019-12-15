from django.test import TestCase as DJTest
from unittest import TestCase

from ..models import Patient, AustinGrid, RoundRockGrid


# models test
class PatientBasicTest(DJTest):
    def create_Patient(self, u_id=1, geom='POINT(0.0 0.0)'):
        # set up a model object
        return Patient.objects.create(u_id=u_id, geom=geom)

    def test_DimDate_creation(self):
        # make sure the data was added to model correctly
        w = self.create_Patient()
        self.assertTrue(isinstance(w, Patient))
        self.assertEqual(w.__str__(), w.u_id)


class FactReviewBasicTest(DJTest):
    def create_Grids(
        self, grid, name=1, mpoly={
  "type": "MultiPolygon",
  "coordinates": [
    [[[102.0, 2.0], [103.0, 2.0], [103.0, 3.0], [102.0, 3.0], [102.0, 2.0]]],
    [[[100.0, 0.0], [101.0, 0.0], [101.0, 1.0], [100.0, 1.0], [100.0, 0.0]],
     [[100.2, 0.2], [100.8, 0.2], [100.8, 0.8], [100.2, 0.8], [100.2, 0.2]]]
  ]
}):
        # same as above but for FactReview model
        if grid == "Austin":
            return AustinGrid.objects.create(name=name, mpoly=mpoly)
        if grid == "RoundRock":
            return RoundRockGrid.objects.create(name=name, mpoly=mpoly)

    def test_FactReview_creation(self):
        w = self.create_FactReview(grid="Austin")
        x = self.create_FactReview(grid="RoundRock")
        self.assertTrue(isinstance(w, AustinGrid))
        self.assertTrue(isinstance(x, RoundRockGrid))
        self.assertEqual(w.__str__(), "Name: 1")
        self.assertEqual(x.__str__(), "Name: 1")