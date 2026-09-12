from django.urls import path, include

urlpatterns = [
    path('v1/', include('api.v1')),
]

app_name = 'api'