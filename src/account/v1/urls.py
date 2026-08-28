from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from account.v1.views.users import  UserList, UserDetail
# user_list, user_detail,

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view())
    ]
