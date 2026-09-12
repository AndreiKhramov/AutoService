from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from automobile.models import Autowork
from automobile.v1.serializers.autoworks import AutoworkSerializer


@extend_schema(tags=["Autoworks"])
class AutoworkViewSet(ModelViewSet):

    queryset = Autowork.objects.all()
    serializer_class = AutoworkSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, *args, **kwargs):
        """
        ## Список работ.
        Разрешения:
        - права - list_user
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        ## Создание работы.
        Разрешения:
        - права - create_user
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        ## Обновление работы.
        Разрешения:
        - права - update_user
        """
        return super().update(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        ## Детальная информация по работе.
        Разрешения:
        - права - update_user
        """
        return super().retrieve(request, args, kwargs)