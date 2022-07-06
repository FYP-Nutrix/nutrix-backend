from django.http import Http404
from nutrition.models import Nutrition, NutritionLogging
from nutrition.serializers import NutritionLogSerializer, NutritionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class NutritionList(APIView):
    """
    API View to create or get a list of all the nutritions.
    Get request will returns the nutritions
    POST request will allow to create a new nutritions
    """

    def get(self, format=None):
        nutritions = Nutrition.objects.all()
        serializer = NutritionSerializer(nutritions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NutritionSerializer(data=request.data)
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

class NutritionDetails(APIView):
    """
    Retrieve, update or delete a nutrition instance.
    Documentation URL: https://www.django-rest-framework.org/tutorial/3-class-based-views/
    """

    def get_object(self, pk):
        try :
            return Nutrition.objects.get(pk=pk)
        except Nutrition.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = NutritionSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = NutritionSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk , format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class NutritionLogList(APIView):
    """
    API View to create or get a list of all the nutrition log.
    Get request will returns the nutrition log
    POST request will allow to create a new nutrition log
    """

    def get(self, format=None):
        nutritions = NutritionLogging.objects.all()
        serializer = NutritionSerializer(nutritions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NutritionLogSerializer(data=request.data)
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
