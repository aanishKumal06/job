from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Role, Profile


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', 'description']


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  
    role = RoleSerializer(read_only=True)   
    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'role', 'created_at', 'updated_at']


class ProfileCreateUpdateSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'full_name', 'role']
