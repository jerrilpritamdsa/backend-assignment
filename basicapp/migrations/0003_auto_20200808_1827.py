# Generated by Django 3.1 on 2020-08-08 12:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20200808_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityperiod',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 18, 27, 26, 765622)),
        ),
        migrations.AlterField(
            model_name='activityperiod',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 18, 27, 26, 765622)),
        ),
    ]
