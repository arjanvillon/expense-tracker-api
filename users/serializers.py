from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import (Wallet,)

class RegisterSerializer(serializers.ModelSerializer):
    """ Serializes registration of a user """

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"],
            validated_data["email"],
            validated_data["password"],
        )

        Wallet.objects.create(owner=user, name="Wallet")

        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")

class WalletSerializer(serializers.ModelSerializer):
    """ Serializes Wallets of user """

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Wallet
        fields = [
            "id",
            "owner",
            "name",
            "balance"
        ]

class UserSerializer(serializers.ModelSerializer):
    """ Serializes User """

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "wallets",
        ]