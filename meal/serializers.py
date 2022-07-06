from rest_framework import serializers
from meal.models import MealImage, MealLogging

class MealImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealImage
        fields = '__all__'

class MealLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = MealLogging
        fields = '__all__'