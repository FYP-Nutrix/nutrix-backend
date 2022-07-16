import uuid
from django.db import models
from meal.models import MealImage

# Create your models here.
class Nutrition(models.Model):
    nutrition_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    meal_name = models.CharField(max_length=255)
    carb = models.DecimalField(max_digits=7, decimal_places=2)
    protein = models.DecimalField(max_digits=7, decimal_places=2)
    fiber = models.DecimalField(max_digits=7, decimal_places=2)
    fats = models.DecimalField(max_digits=7, decimal_places=2)
    water = models.DecimalField(max_digits=7, decimal_places=2)
    mineral = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_a = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_b = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_c = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_d = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_e = models.DecimalField(max_digits=7, decimal_places=2)
    vitamin_k = models.DecimalField(max_digits=7, decimal_places=2)
    calorie_per_serving = models.IntegerField()
    serving_size = models.DecimalField(max_digits=7, decimal_places=2)
    serving_type = models.CharField(max_length=255)
    serving_gram = models.DecimalField(max_digits=7, decimal_places=2)

class NutritionLogging(models.Model):
    nutrition_logging_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    meal_image = models.ForeignKey(MealImage, on_delete=models.CASCADE)
    nutrition = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
