from os import name
from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command seeds facilities."

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
            "EV charger",
        ]
        for f in facilities:
            room_models.Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created!"))
