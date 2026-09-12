from django.urls import include, path

urlpatterns = [
    path("accounts/", include("account.v1.urls")),
    path("automobiles/", include("automobile.v1.urls")),
    path("orders/", include("order.v1.urls")),
]

app_name = "v1"