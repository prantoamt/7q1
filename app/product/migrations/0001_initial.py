# Generated by Django 4.1.5 on 2023-01-22 16:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        db_column="product_id",
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Product ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=256, unique=True, verbose_name="Name"),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="Is deleted"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Updated At"),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
                "db_table": "Product",
            },
        ),
    ]
