# Python imports
from typing import Any

# Third party imports
from django.db.models.query import QuerySet
from rest_framework import request

# Self imports
from company.models import Company
from companyproduct.models import CompanyProduct


class CompanyService:
    model = Company

    def get_queryset(self, *args: tuple[str], **kwargs: dict[str, str]):
        return Company.objects.filter(**kwargs)

    def _fetch_company_ids_by_product_name(self, names: list[str]) -> list[QuerySet]:
        company_ids = CompanyProduct.objects.filter(
            product__name__in=names
        ).values_list("company_id")
        return company_ids

    def build_kwargs_for_query(self, request: request):
        kwargs = {}
        product_names = request.query_params.getlist("product")
        if len(product_names) > 0:
            company_ids = self._fetch_company_ids_by_product_name(names=product_names)
            kwargs["id__in"] = company_ids
        return kwargs
