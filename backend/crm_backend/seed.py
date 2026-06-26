import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE','crm_backend.settings')
django.setup()

from lead.models import Lead
from team.models import Team
from django.contrib.auth.models import User


fake = Faker()

def create_seed_data(n=20):
    users = User.objects.all()
    teams = Team.objects.all()

    if not users.exists() or not teams.exists():
        print('Error: No users or team exists in the database !')
        return


    for _ in range(n):
        user = random.choice(users)
        team = random.choice(teams)

        lead = Lead.objects.create(
            team = team,
            company = fake.company(),
            contact_person = fake.name(),
            email = fake.email(),
            phone = fake.phone_number()[:20],#limiting the lenght
            website = fake.url(),
            status = Lead.NEW,
            confidence = 5,
            priority = Lead.LOW,
            estimated_value = fake.random_int(1000,500000),
            assigned_to = random.choice(users),
            created_by = user,

        )


if __name__ == '__main__':
    create_seed_data(15)

