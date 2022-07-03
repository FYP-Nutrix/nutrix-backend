from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from nutrition.models import Nutrition

class NutritionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrition
        fields = '__all__'
