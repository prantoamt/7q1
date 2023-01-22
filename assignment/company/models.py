# Python imports
import uuid
from django.db import models

# Third party imports

# Self imports
from product.models import Product


class Company(models.Model):
    id = models.UUIDField(
        db_column="company_id",
        verbose_name="Company ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=256, unique=True, verbose_name="Name")
    url = models.CharField(max_length=256, verbose_name="Url")
    country = models.CharField(max_length=256, verbose_name="Country")
    is_deleted = models.BooleanField(default=False, verbose_name="Is deleted")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name_plural = "Companies"
        db_table = "Company"

    def __str__(self) -> str:
        return self.name


class CompanyProduct(models.Model):
    iid = models.UUIDField(
        db_column="company_product_id",
        verbose_name="Company Product ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    company = models.ForeignKey(
        'company.Company', on_delete=models.CASCADE, verbose_name='Company', related_name='products')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='Product', related_name='companies')
    
    class Meta:
        verbose_name_plural = 'Company products'
        db_table = 'CompanyProducts'

    def __str__(self) -> str:
        return self.company.name