from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Job


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class JobSerializer(serializers.ModelSerializer):
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            'id', 'title', 'description', 'location', 'company',
            'posted_by', 'is_active', 'posted_at', 'updated_at',
            'salary_min', 'salary_max', 'job_type'
        ]


class JobCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = [
            'title', 'description', 'location', 'company',
            'is_active', 'salary_min', 'salary_max', 'job_type'
        ]
