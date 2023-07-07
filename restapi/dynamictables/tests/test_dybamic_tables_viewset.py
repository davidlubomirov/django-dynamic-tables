import os

from rest_framework import status
from rest_framework.test import APITestCase

from django.urls import reverse
from django.urls.exceptions import NoReverseMatch
from django import setup

from dynamictables.urls import router as dynamic_tables_router
from dynamictables.views import DynamicTablesViewSet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restapi.settings')
setup()


class TestDynamicTablesViewSet(APITestCase):
    def test_viewset_list(self):
        url: str = reverse("dynamic-tables-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_viewset_create(self):
        url: str = reverse("dynamic-tables-list")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_viewset_update(self):
        url: str = reverse("dynamic-tables-detail", kwargs={"pk": 1})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_viewset_row_create(self):
        url: str = reverse("dynamic-tables-row", kwargs={"pk": 1})
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_viewset_rows_get(self):
        url: str = reverse("dynamic-tables-rows", kwargs={"pk": 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
