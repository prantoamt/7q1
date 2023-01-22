# Python imports
from typing import Any
# Django imports
from django.db.models.query import QuerySet
from company.models import Company

# Self imports
from companyproduct.models import CompanyProduct

class CompanyService:
    model = Company

    def get_queryset(self, *args:tuple[str], **kwargs: dict[str, str]):
        return Company.objects.filter(**kwargs)

    def fetch_company_ids_by_product_name(self, names: list[str]) -> list[QuerySet] :
        company_ids = CompanyProduct.objects.filter(product__name__in=names).values_list('company_id')
        return company_ids