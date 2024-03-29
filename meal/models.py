from distutils.command.upload import upload
from pyexpat import model
from uuid import uuid4
from django.db import models
import uuid
from user.models import Account

# Create your models here.
# meal type for user to choose for each entry
MEAL_TYPE = [
    ('BREAKFAST','Breakfast'),
    ('LUNCH','Lunch'),
    ('DINNER','Dinner'),
    ('SUPPER','Supper'),
    ('OTHER','Other'),
]

# User meal loggin for each meal
class MealLogging(models.Model):
    meal_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=20)
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        naming = self.user.email + " " + self.meal_type
        return naming

# Store Meal Image
class MealImage(models.Model):
    image_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, null=False)
    meal_image = models.ImageField(null=False, upload_to="meal_logging")
    meal_name = models.CharField(max_length=100, null=True)
    total_calorie = models.IntegerField(null=True)
    meal_size = models.DecimalField(max_digits=7, decimal_places=2,null=True)
    meal_logging = models.ForeignKey(MealLogging, related_name='meal_image',on_delete=models.CASCADE)