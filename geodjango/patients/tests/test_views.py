from django.conf import settings
from django.urls import reverse, resolve
from django.test import TestCase as DJTest
from rest_framework.test import APIRequestFactory

from ..views import index
from ..models import Patient, RoundRockGrid, AustinGrid


class UrlTests(DJTest):

    def render_template(self):
        # ensures that rendering the template goes to the correct page, gives 200 code, and uses correct html template

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")