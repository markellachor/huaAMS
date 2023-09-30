from django.contrib.auth import get_user_model
from rest_framework import serializers
from api.models import Profile

UserModel = get_user_model()

from api.models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            is_staff=validated_data["is_staff"],
            is_superuser=validated_data["is_superuser"],
            is_active=validated_data["is_active"],
        )

        return user

    class Meta:
        model = UserModel
        fields = [
            "id",
            "username",
            "password",
            "email",
            "first_name",
            "last_name",
            "is_staff",
            "is_superuser",
            "is_active",
            "profile"
        ]
