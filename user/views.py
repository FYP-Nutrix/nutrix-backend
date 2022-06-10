from django.shortcuts import render
from user.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.
def index(request):
    return render(request,"index.html")

class UserRecordView(APIView):
    """
    API View to create or get a list of all the registered users.
    Get request will returns the registered users
    POST request will allow to create a new users
    """

    @authentication_classes([JWTAuthentication])
    def get(self, format=None):
        users = get_user_model()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @authentication_classes([])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            serializer.validated_data
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages
            },
            status=status.HTTP_400_BAD_REQUEST
        )