# Python imports
import uuid
from django.db import models

# Third party imports

# Self imports


class CompanyProduct(models.Model):
    iid = models.UUIDField(
        db_column="company_product_id",
        verbose_name="Company Product ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    company = models.ForeignKey(
        "company.Company",
        on_delete=models.CASCADE,
        verbose_name="Company",
        related_name="products",
    )
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        verbose_name="Product",
        related_name="companies",
    )
    is_deleted = models.BooleanField(default=False, verbose_name="Is deleted")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")


    class Meta:
        unique_together = [['company', 'product']]
        verbose_name_plural = "Company products"
        db_table = "CompanyProducts"

    def __str__(self) -> str:
        return self.company.name
