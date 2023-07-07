from django.urls import path

from .views import DynamicTablesViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r"api/table", DynamicTablesViewSet, basename="dynamic-tables")
