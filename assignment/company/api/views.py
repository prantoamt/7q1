# Python imports

# Third party imports
from urllib import request
from django.db.models.query import QuerySet
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import AllowAny, IsAuthenticated

# self imports
from .serializers import CompanySerializer
from company.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    lookup_field = "id"
    http_method_names = ["get"]

    def get_queryset(self, **kwargs) -> QuerySet:
        return self.model.objects.filter(**kwargs)

    def list(self, request: request, *args: tuple, **kwargs: dict) -> Response:
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: request, *args: tuple, **kwargs: dict) -> Response:
        return super().retrieve(request, *args, **kwargs)
