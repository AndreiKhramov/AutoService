from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from automobile.models import Automobile
from automobile.v1.serializers.automobiles import AutoSerializer


@extend_schema(tags=["Automobiles"])
class AutoViewSet(ModelViewSet):

    queryset = Automobile.objects.all()
    serializer_class = AutoSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, *args, **kwargs):
        """
        ## Список автомобилей.
        Разрешения:
        - права - list_user
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        ## Создание автомобиля.
        Разрешения:
        - права - create_user
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        ## Обновление автомобиля.
        Разрешения:
        - права - update_user
        """
        return super().update(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        ## Детальная информация по автомобилю.
        Разрешения:
        - права - update_user
        """
        return super().retrieve(request, args, kwargs)