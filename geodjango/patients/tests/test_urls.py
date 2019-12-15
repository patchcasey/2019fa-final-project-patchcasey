from django.conf import settings
from django.urls import reverse, resolve
from django.test import TestCase as DJTest
from ..views import index


class UrlTests(DJTest):
    def test_view_url_exists_at_desired_location(self):
        # ensures the urls are all reachable pages
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_base_url(self):
        # ensures the home URL is correct
        response2 = self.client.get("/")
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(resolve("/").url_name, "index")