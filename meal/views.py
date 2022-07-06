from django.http import Http404
from django.shortcuts import render
from meal.models import MealImage, MealLogging
from meal.serializers import MealImageSerializer, MealLogSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class MealImageList(APIView):
    """
    API View to create or get a list of all the meal image
    Get request will returns the meal image
    POST request will allow to create a new meal image
    """

    def get(self, format=None):
        meal_image = MealImage.objects.all()
        serializer = MealImageSerializer(meal_image, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealImageSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save() # create data
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

class MealImageDetails(APIView):
    """
    Retrieve, update or delete a nutrition instance.
    Documentation URL: https://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get_object(self, pk):
        try :
            return MealImage.objects.get(pk=pk)
        except MealImage.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MealImageSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = MealImageSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk , format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MealLogList(APIView):
    """
    API View to create or get a list of all the meal log.
    Get request will returns the meal log
    POST request will allow to create a new meal log
    """

    def get(self, format=None):
        meal_log = MealLogging.objects.all()
        serializer = MealLogSerializer(meal_log, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealLogSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.save() # create data
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

