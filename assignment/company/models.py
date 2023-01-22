# Python imports
import uuid
from django.db import models

# Third party imports

# Self imports


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
    is_deleted = models.BooleanField(default=True, verbose_name="Is deleted")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name_plural = "Companies"
        db_table = "Company"

    def __str__(self) -> str:
        return self.name
