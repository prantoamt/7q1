from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework import routers

from company.api.views import CompanyViewSet

router = routers.DefaultRouter()

router.register(r"", CompanyViewSet, "companies")

urlpatterns = [
    path("/", include(router.urls)),
]
