from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import User
from account.v1.serializers.users import UserSerializer, UserFuncSerializer

from rest_framework import permissions, viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# @api_view(["GET", "POST"])
# def user_list(request):
#     """
#     List all code users, or create a new user.
#     """
#     if request.method == "GET":
#         users = User.objects.all()
#         serializer = UserFuncSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == "POST":
#         serializer = UserFuncSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def user_detail(request, pk):
#     """
#     Retrieve, update or delete a code user.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == "GET":
#         serializer = UserFuncSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == "PUT":
#         serializer = UserFuncSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == "DELETE":
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(APIView):
    """
    List all users, or create a new user.
    """
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserFuncSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserFuncSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetail(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserFuncSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
