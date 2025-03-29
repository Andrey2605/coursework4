from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand, call_command


class Command(BaseCommand):
    def handle(self, *args, **options):
        fixtures_dir = settings.BASED_DIR/"fixtures"
        fixtures = [
            'group.json'
        ]

        for fixtures_name in fixtures:
            call_command('loaddata', fixtures_dir/fixtures_name)

            self.stdout.write(self.style.SUCCESS('Successfully loaded fixtures'))