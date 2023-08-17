from django.db import models
from rest_framework import serializers

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerUser
        fields = '__all__'
