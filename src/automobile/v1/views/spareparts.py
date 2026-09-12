from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from automobile.models import Sparepart
from automobile.v1.serializers.spareparts import SparepartSerializer


@extend_schema(tags=["Spareparts"])
class SparepartViewSet(ModelViewSet):

    queryset = Sparepart.objects.all()
    serializer_class = SparepartSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, *args, **kwargs):
        """
        ## Список запчатей.
        Разрешения:
        - права - list_user
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        ## Создание запчати.
        Разрешения:
        - права - create_user
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        ## Обновление запчати.
        Разрешения:
        - права - update_user
        """
        return super().update(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        ## Детальная информация по запчати.
        Разрешения:
        - права - update_user
        """
        return super().retrieve(request, args, kwargs)