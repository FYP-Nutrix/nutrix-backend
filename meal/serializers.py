from rest_framework import serializers
from meal.models import MealImage, MealLogging

class MealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields = ['image_id','meal_image','total_calorie','meal_size']

class MealLogSerializer(serializers.ModelSerializer):
    meal_image = MealImageSerializer(many=True)

    class Meta:
        model = MealLogging
        fields = '__all__'

    def create(self, validated_data):
        meal_image = validated_data.pop('meal_image')
        print("Meal Image is here: ", meal_image)
        meal_log = MealLogging.objects.create(**validated_data)
        for meal_image in meal_image:
            MealImage.objects.create(meal_logging=meal_log, **meal_image)
        return meal_log