from administration.models import User
from django.core.management.base import BaseCommand
from django.conf import settings

BASE_DIR = settings.BASE_DIR


class Command(BaseCommand):
    help = "Creates user for demo"

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username='john')
        user.set_password('j123j123')
        user.save()
        if created:
            self.stdout.write(
            self.style.SUCCESS(f'User created with username {user.username}')
        )
        else:
            self.stdout.write(
            self.style.WARNING(f'User with username {user.username} already exists')
        )    