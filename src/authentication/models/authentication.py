from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

from authentication.jwt_store import is_token_active


class RedisJWTAuthentication(JWTAuthentication):
    def get_validated_token(self, raw_token):
        validated_token = super().get_validated_token(raw_token)

        if not is_token_active(validated_token):
            raise InvalidToken(
                "Токен отозван или отсутствует в Redis."
            )

        return validated_token