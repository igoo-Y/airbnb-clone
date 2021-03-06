import random
from os import name
from django.core.management.base import BaseCommand
from django.db import models
from django_seed import Seed
from users import models as user_models
from rooms import models as room_models
from reviews import models as review_models


class Command(BaseCommand):

    help = "This command makes many reviews."

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many reviews you want to create?"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder = Seed.seeder()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "review": lambda x: seeder.faker.sentence(),
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reviews created!"))
