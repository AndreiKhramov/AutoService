from rest_framework.routers import SimpleRouter
from order.v1.views.orders import OrderViewSet

router = SimpleRouter()
router.register("order", OrderViewSet, basename="order")

urlpatterns = router.urls

app_name = "order"