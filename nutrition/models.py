import uuid
from django.db import models
from meal.models import MealImage

# Create your models here.
class NutritionData(models.Model):
    nutrition_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    nutrition_name = models.CharField(max_length=255)
    nutrition_unit = models.CharField(max_length=255)


class Nutrients(models.Model):
    nutrient_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    nutrient_name = models.CharField(max_length=255)
    nutrient_value = models.IntegerField()
    meal_image = models.ForeignKey(MealImage, on_delete=models.CASCADE)

class NutritionLogging(models.Model):
    nutrition_logging_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    meal_image = models.ForeignKey(MealImage, on_delete=models.CASCADE)
