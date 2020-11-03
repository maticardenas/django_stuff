import os
# Settings of the project, before manupulating actual models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "level_two_project.settings")

import django
django.setup()

import random
from main_app.models import User
from faker import Faker

fake_gen: Faker = Faker()

def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry

        domains = ["com", "net", "gov"]

        # Create fake data
        fake_name = fake_gen.name().split()[0]
        fake_last_name = fake_gen.name().split()[1]
        fake_email = f"{fake_gen.name().lower()}@{fake_gen.company().lower()}.{random.choice(domains)}"

        # Create web page entry
        user = User.objects.get_or_create(
            first_name=fake_name,
            last_name=fake_last_name,
            email=fake_email
        )[0]
        user.save()


if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating complete!")