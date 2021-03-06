from .models import User, ActivityPeriod
from rest_framework import serializers


class ActivitySerializer(serializers.ModelSerializer):

    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):

    activity_periods = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']
