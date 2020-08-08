import pytz
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    TIMEZONE_CHOICE = tuple([(i, i) for i in pytz.all_timezones])

    id = models.CharField(max_length=15, unique=True, primary_key=True)
    username = models.CharField(max_length=256, unique=True)
    real_name = models.CharField(max_length=256)
    tz = models.CharField(max_length=256, choices=TIMEZONE_CHOICE)
    date_joined = models.DateTimeField(
        verbose_name="date joined",
        auto_now_add=True
    )
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['id', 'tz', 'real_name']

    def __str__(self):
        return self.real_name

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)

    @property
    def activity_periods(self):
        return self.activityperiod_set.all()


class ActivityPeriod(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=datetime.now())
    end_time = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.user.real_name
