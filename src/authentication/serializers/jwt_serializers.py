from rest_framework import serializers

from authentication.jwt_store import (is_token_active, register_token, revoke_token)
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework_simplejwt.serializers import (TokenObtainPairSerializer, TokenRefreshSerializer)
from rest_framework_simplejwt.exceptions import InvalidToken


class RedisTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        access_token = AccessToken(data["access"])
        refresh_token = RefreshToken(data["refresh"])

        register_token(access_token)
        register_token(refresh_token)

        return data

class RedisTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        old_refresh = RefreshToken(attrs["refresh"])

        if not is_token_active(old_refresh):
            raise InvalidToken(
                "Refresh-токен отозван или отсутствует в Redis."
            )

        data = super().validate(attrs)

        register_token(AccessToken(data["access"]))

        if "refresh" in data:
            revoke_token(old_refresh)
            register_token(RefreshToken(data["refresh"]))

        return data

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(write_only=True)