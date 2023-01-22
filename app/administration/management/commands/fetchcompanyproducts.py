# Python imports
import csv, os, ast

# Third party imports
from django.core.management.base import BaseCommand
from django.conf import settings

# Self imports
from product.models import Product
from company.models import Company
from companyproduct.models import CompanyProduct

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    product_file_path = os.path.join(BASE_DIR, "files", "company_products.csv")
    help = "Creates company products from provided file"

    def create_company_product(self, company: Company, product: Product) -> tuple:
        return CompanyProduct.objects.get_or_create(company=company, product=product)

    def get_company(self, name: str) -> Company:
        return Company.objects.filter(
            name=name,
        ).first()

    def get_product(self, name: str) -> Product:
        return Product.objects.filter(name=name).first()

    def handle(self, *args, **options):
        with open(self.product_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            total_created = 0
            for row in csv_reader:
                company_name = row.get("name")
                company = self.get_company(name=company_name)
                if not company:
                    self.stdout.write(
                        self.style.WARNING(
                            'Company "%s" does not exist in database' % company_name
                        )
                    )
                    continue
                products_for_the_company = ast.literal_eval(row.get("products"))
                for product_name in products_for_the_company:
                    product = self.get_product(name=product_name)
                    if not product:
                        self.stdout.write(
                            self.style.WARNING(
                                'Product "%s" does not exist in database' % product_name
                            )
                        )
                        continue
                    company_product, created = self.create_company_product(
                        company=company, product=product
                    )
                if created:
                    total_created += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Successfully created product "{product_name}" for company "{company_name}"'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'product "{product_name}" already exists for company "{company_name}"'
                        )
                    )

        self.stdout.write(
            self.style.SUCCESS(f'Total "{total_created}" company products created')
        )
