from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView)
from authentication.jwt_store import is_token_active, revoke_token
from authentication.serializers.jwt_serializers import (LogoutSerializer, RedisTokenObtainPairSerializer, RedisTokenRefreshSerializer)


@extend_schema(tags=["Authentication"])
class RedisTokenObtainPairView(TokenObtainPairView):
    serializer_class = RedisTokenObtainPairSerializer


@extend_schema(tags=["Authentication"])
class RedisTokenRefreshView(TokenRefreshView):
    serializer_class = RedisTokenRefreshSerializer


@extend_schema(tags=["Authentication"])
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=LogoutSerializer,
        responses={204: None},
        description="Отзывает access и refresh JWT-токены.",
    )
    def post(self, request):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            refresh_token = RefreshToken(
                serializer.validated_data["refresh"]
            )
        except TokenError as error:
            raise InvalidToken("Некорректный refresh-токен.") from error

        if not is_token_active(refresh_token):
            raise InvalidToken("Refresh-токен уже отозван.")

        user_id_claim = api_settings.USER_ID_CLAIM
        user_id_field = api_settings.USER_ID_FIELD

        token_user_id = refresh_token.get(user_id_claim)
        current_user_id = getattr(request.user, user_id_field)

        if str(token_user_id) != str(current_user_id):
            raise InvalidToken(
                "Refresh-токен принадлежит другому пользователю."
            )

        revoke_token(refresh_token)

        if request.auth:
            revoke_token(request.auth)

        return Response(status=status.HTTP_204_NO_CONTENT)
