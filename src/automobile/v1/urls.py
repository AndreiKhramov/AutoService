from rest_framework.routers import SimpleRouter
from automobile.v1.views.automobiles import AutoViewSet
from automobile.v1.views.autoworks import AutoworkViewSet
from automobile.v1.views.spareparts import SparepartViewSet

router = SimpleRouter()
router.register("automobile", AutoViewSet, basename="automobile")
router.register("autowork", AutoworkViewSet, basename="autowork")
router.register("sparepart", SparepartViewSet, basename="sparepart")

urlpatterns = router.urls

app_name = "automobile"