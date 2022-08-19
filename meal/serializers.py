from dataclasses import field
from rest_framework import serializers
import meal
from meal.api import requestImageName
from meal.models import MealImage, MealLogging
from user.models import Account
from user.serializers import UserSerializer
from django.db.models import Sum

class MealImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealImage
        fields = ['image_id','meal_image','total_calorie','meal_size','meal_name']

class MealLogSerializer(serializers.ModelSerializer):
    meal_image = MealImageSerializer(many=True)

    class Meta:
        model = MealLogging
        fields = '__all__'

    def create(self, validated_data):
        meal_image = validated_data.pop('meal_image')
        meal_log = MealLogging.objects.create(**validated_data)
        for meal_image in meal_image:
            image_url = meal_image['meal_image']
            food_name = requestImageName(image_url)
            meal_image = MealImage.objects.create(meal_logging=meal_log, **meal_image, meal_name=food_name)
        return meal_log

class MealPatientCalorieSerializer(serializers.ModelSerializer):
    meal_total_calorie = serializers.IntegerField()
    user =  UserSerializer()

    def get_patient_total_calorie(self):
        user = Account.objects.get(id=self)
        patient_log = MealLogging.objects.filter(user = user)
        patient_total_calorie = MealImage.objects.filter(meal_logging__in=[a.meal_id for a in patient_log]).aggregate(Sum('total_calorie'))
        meal_total_calorie = patient_total_calorie['total_calorie__sum']
        return meal_total_calorie