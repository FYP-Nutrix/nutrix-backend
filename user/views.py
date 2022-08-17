from django.http import Http404
from django.shortcuts import render
from user.serializers import MealSettingSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from user.models import Account, MealSetting

# Create your views here.
def index(request):
    return render(request,"index.html")

class UserList(APIView):
    """
    API View to create or get a list of all the registered users.
    Get request will returns the registered users
    POST request will allow to create a new users
    """

    @authentication_classes([JWTAuthentication])
    def get(self, format=None):
        users = Account.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    @authentication_classes([])
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data) # create data
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

class UserDetails(APIView):
    """
    Retrieve, update or delete a user instance.
    Documentation URL: https://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get_object(self, pk):
        try :
            return Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        password = request.data.get('password')
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid(): 
            if password != '': 
                serializer.save()
                new_password = serializer.validated_data.get('password')
                if new_password: 
                    user.set_password(new_password)
                    user.save()
                
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk , format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealSettingList(APIView):
    """
    API View to create or get a list of all the meal setting of registered patients.
    Get request will returns the meal setting of registered patients
    POST request will allow to create a new meal setting for registered patients
    """

    def get(self, format=None):
        setting = MealSetting.objects.all()
        serializer = MealSettingSerializer(setting, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = MealSettingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
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

class MealSettingDetails(APIView):
    """
    Retrieve, update or delete a patient instance.
    Documentation URL: https://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get_object(self, pk):
        try :
            return MealSetting.objects.get(account=pk)
        except MealSetting.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MealSettingSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        # if request.data['advice'] == '':
        #     request.data['advice'] = None
        serializer = MealSettingSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk , format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)