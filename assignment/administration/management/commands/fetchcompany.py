import json, csv, os
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from company.models import Company

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    company_file_path = os.path.join(BASE_DIR, "files", "companies.csv")
    print(company_file_path, "======")
    help = "Created companies from provided file"

    def handle(self, *args, **options):
        with open(self.company_file_path) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            total_created = 0
            for row in csv_reader:
                company, created = Company.objects.get_or_create(
                    name=row.get("name"),
                    defaults={"country": row.get("country"), "url": row.get("url")},
                )
                if created:
                    total_created += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            'Successfully created company "%s"' % company.name
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.SUCCESS('Company "%s" already exists' % company.name)
                    )

        self.stdout.write(
            self.style.SUCCESS('Total "%s" company created' % total_created)
        )
