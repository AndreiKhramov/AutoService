from django.urls import path
from authentication.views.jwt_views import (LogoutView, RedisTokenObtainPairView, RedisTokenRefreshView)

urlpatterns = [
    path("token/", RedisTokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("token/refresh/", RedisTokenRefreshView.as_view(), name="token-refresh"),
    path("token/logout/", LogoutView.as_view(), name="token-logout")
    ]
