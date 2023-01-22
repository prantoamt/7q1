from rest_framework.authtoken import views
from django.urls import path, include
from rest_framework import routers

from ..company.api.views import CompanyViewSet

router = routers.DefaultRouter()

router.register(r"companies", CompanyViewSet, "companies")

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
]
