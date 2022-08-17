from rest_framework import serializers
from meal.models import MealImage
from meal.serializers import MealImageSerializer
from nutrition.models import Nutrition, NutritionLogging

class NutritionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nutrition
        fields = '__all__'

class NutritionLogSerializer(serializers.ModelSerializer):
    meal_image = MealImageSerializer(required=False)
    nutrition = NutritionSerializer(required=False)

    class Meta:
        model = NutritionLogging
        fields = '__all__'
    
    def create(self, validated_data):
        meal = MealImage.objects.all()
        nutritions = Nutrition.objects.all()
        for nut in nutritions:
            for m in meal:
                if nut.meal_name == m.meal_name:
                    print(nut.meal_name)
                    meal_image = MealImage.objects.get(meal_name=m.meal_name)
                    nutrition = Nutrition.objects.get(meal_name=nut.meal_name)
                    nut_log = NutritionLogging.objects.create(meal_image=meal_image, nutrition=nutrition)
        return nut_log