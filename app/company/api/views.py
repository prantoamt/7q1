# Python imports
from typing import Any

# Third party imports
from rest_framework import request
from rest_framework.response import Response
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# self imports
from .serializers import CompanySerializer
from company.models import Company
from .services import CompanyService


class CompanyViewSet(viewsets.ModelViewSet):
    model = Company
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = "id"
    http_method_names = ["get"]

    def __init__(self, company_service=CompanyService(), **kwargs: dict[Any]) -> None:
        self.company_service = company_service
        super().__init__(**kwargs)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="product",
                description="filter by product",
                required=False,
                type=str,
                style="form",
                location=OpenApiParameter.QUERY,
                explode=False,
                examples=[
                    OpenApiExample(
                        "Example 1",
                        summary="Filters by the product keyword",
                        description='Client can pass multiple value for product by appending &prodcut="product name" in query string',
                        value="HIGH PRESSURE HOSES",
                    )
                ],
            )
        ]
    )
    def list(self, request: request, *args: tuple, **kwargs: dict) -> Response:
        kwargs = self.company_service.build_kwargs_for_query(request=request)
        queryset = self.company_service.get_queryset(**kwargs)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(data=serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: request, *args: tuple, **kwargs: dict) -> Response:
        return super().retrieve(request, *args, **kwargs)
