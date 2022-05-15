from tkinter.tix import Tree
from django.db import models
import uuid

# Create your models here.
class FoodType(models.Model):
    food_id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    food_type = models.CharField(max_length=200, unique=True) 

class FoodLabel(models.Model):
    food_label_id = models.UUIDField(default=uuid.uuid4, primary_key=True, null=False)
    food_image_path = models.ImageField(null=True, blank=True, upload_to="img/food", verbose_name='Food Upload')
    food = models.ForeignKey(FoodType, on_delete=models.CASCADE, null=True)