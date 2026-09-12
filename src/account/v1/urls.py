from rest_framework.routers import SimpleRouter
from account.v1.views.users import UserViewSet


router = SimpleRouter()
router.register("user", UserViewSet, basename="user")

urlpatterns = router.urls

app_name = "accounts"