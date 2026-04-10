from django.urls import path, include

from .views import ManufactureViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("manufactures", ManufactureViewSet, basename="manufacture")

urlpatterns = [
    path("", include(router.urls)),
]
