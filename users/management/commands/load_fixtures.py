from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand




class Command(BaseCommand):
    def handle(self, *args, **options):
        fixtures_dir = settings.BASED_DIR/"fixtures"
        fixtures