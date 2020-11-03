import os
# Settings of the project, before manupulating actual models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "second_project.settings")

import django
django.setup()

import random
from second_app.models import AccessRecord, WebPage, Topic
from faker import Faker

fake_gen = Faker()

topics = ["Search", "Social", "Marketplace", "News", "Games"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # Get the topic for the entry
        top = add_topic()

        # Create fake data
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # Create web page entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create fake access record
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':
    print("Populating script!")
    populate(10)
    print("Populating complete!")