from os import name
from django.core.management.base import BaseCommand
from rooms import models as room_models


class Command(BaseCommand):

    help = "This command seeds amenities."

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Iron",
            "Hair dryer",
            "Dedicated workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
            "Beachfront",
            "Waterfront",
        ]
        for a in amenities:
            room_models.Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
