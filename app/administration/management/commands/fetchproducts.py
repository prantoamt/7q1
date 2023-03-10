import csv, os
from django.core.management.base import BaseCommand
from django.conf import settings
from product.models import Product

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    product_file_path = os.path.join(BASE_DIR, "files", "products.csv")
    help = "Creates products from provided file"

    def handle(self, *args, **options):
        with open(self.product_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            total_created = 0
            for row in csv_reader:
                product, created = Product.objects.get_or_create(
                    name=row.get("name"),
                    defaults={"is_deleted": False},
                )
                if created:
                    total_created += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            'Successfully created product "%s"' % product.name
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS('product "%s" already exists' % product.name)
                    )

        self.stdout.write(
            self.style.SUCCESS('Total "%s" products created' % total_created)
        )
