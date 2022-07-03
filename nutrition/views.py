from nutrition.models import Nutrition
from nutrition.serializers import NutritionSerializer
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
