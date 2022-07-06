from rest_framework import serializers
from nutrition.models import Nutrition, NutritionLogging

class NutritionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrition
        fields = '__all__'

class NutritionLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = NutritionLogging
        fields = '__all__'