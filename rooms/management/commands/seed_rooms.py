from os import name
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms.models import Room


class Command(BaseCommand):

    help = "This command makes many rooms."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many rooms you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(
            Room,
            number,
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
