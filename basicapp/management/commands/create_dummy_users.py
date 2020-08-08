import pytz
import random
import string
from datetime import datetime
from faker import Faker
from basicapp.models import User, ActivityPeriod
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = 'Adds dummy users'

    def create_users(self, number_of_fakes):

        fake = Faker()

        for _ in range(number_of_fakes):
            ids = ''.join(
                random.choice(
                    string.ascii_uppercase + string.digits
                ) for _ in range(9)
            )
            name = fake.name()
            username = name.lower().replace(' ', '_')
            tz = random.choice([i for i in pytz.all_timezones])
            user = User.objects.create(
                id=ids, real_name=name, tz=tz, username=username
            )
            user.refresh_from_db()
            ActivityPeriod.objects.create(
                user_id=user.id,
                start_time=datetime.now(),
                end_time=datetime.now()
            )
            ActivityPeriod.objects.create(
                user_id=user.id,
                start_time=datetime.now(),
                end_time=datetime.now()
            )
            ActivityPeriod.objects.create(
                user_id=user.id,
                start_time=datetime.now(),
                end_time=datetime.now()
            )
            print("data is polulated")

    def handle(self, *args, **options):
        self.create_users(50)
