from rest_framework import serializers

from ProjectManagement.accounts.models import WorkerUser
from ProjectManagement.projects.models import Task


class WorkerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerUser
        fields = '__all__'


class WorkerUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerUser
        fields = ['is_active']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
