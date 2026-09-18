from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from products.models import Category
import os


class Command(BaseCommand):
    help = 'One-time production setup: categories + superuser'

    def handle(self, *args, **kwargs):
        categories = ["Accessories", "Beauty", "Electronics", "Fashion", "Groceries", "Home Food", "Luggage", "Mobiles", "Shoes"]
        for name in categories:
            Category.objects.get_or_create(name=name)
        self.stdout.write(self.style.SUCCESS('Categories ready'))

        username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        if username and not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS(f'Superuser {username} created'))
        else:
            self.stdout.write('Superuser already exists or env vars missing, skipping')