from django.urls import path

from account.v1.views.users import  UserList, UserDetail

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view())
    ]
