from rest_framework import serializers
from .models import Application
from users.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'full_name', 'user', 'role']


class ApplicationSerializer(serializers.ModelSerializer):
    job = serializers.StringRelatedField()
    applicant = ProfileSerializer(read_only=True)

    class Meta:
        model = Application
        fields = [
            'id', 'job', 'applicant', 'cover_letter', 'resume',
            'status', 'applied_at', 'updated_at'
        ]


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['job', 'cover_letter', 'resume']
