from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.v1.serializers.orders import OrderSerializer


@extend_schema(tags=["Orders"])
class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    http_method_names = ["get", "post", "put", "delete"]

    def list(self, request, *args, **kwargs):
        """
        ## Список заказов.
        Разрешения:
        - права - list_user
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        ## Создание заказа.
        Разрешения:
        - права - create_user
        """
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        """
        ## Обновление заказа.
        Разрешения:
        - права - update_user
        """
        return super().update(request, args, kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        ## Детальная информация по заказу.
        Разрешения:
        - права - update_user
        """
        return super().retrieve(request, args, kwargs)