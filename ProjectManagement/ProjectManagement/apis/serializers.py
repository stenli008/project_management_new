from rest_framework import serializers

from ProjectManagement.accounts.models import WorkerUser


class WorkerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerUser
        fields = '__all__'


class WorkerUserStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerUser
        fields = ['is_active']
