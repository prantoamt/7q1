# Python imports
import uuid
from django.db import models

# Third party imports

# Self imports


class Product(models.Model):
    id = models.UUIDField(
        db_column="product_id",
        verbose_name="Product ID",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    name = models.CharField(max_length=256, unique=True, verbose_name="Name")

    is_deleted = models.BooleanField(default=False, verbose_name="Is deleted")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name_plural = "Products"
        db_table = "Product"

    def __str__(self) -> str:
        return self.name
