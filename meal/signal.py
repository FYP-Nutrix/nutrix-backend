from django.db.models.signals import post_save, pre_save
from meal.models import MealImage
from django.dispatch import receiver

from nutrition.models import Nutrition, NutritionLogging

@receiver(post_save, sender=MealImage)
def generate_nutrition(sender, **kwargs):
    if sender == MealImage:
        instance = kwargs['instance']
        # use the instance meal name to find the food name in nutrition table
        new_meal_name = instance.meal_name
        try:
            nutrition_info = Nutrition.objects.get(meal_name=new_meal_name)
            # to get back the previous meal information entry
            meal_image_id = instance.image_id
            meal_image_obj = MealImage.objects.get(image_id=meal_image_id)
            data = NutritionLogging(meal_image=meal_image_obj,nutrition=nutrition_info)
            data.save()
        except Nutrition.DoesNotExist:

            print("no data")

    else :
        print("something is wrong")

@receiver(post_save, sender=NutritionLogging)
def generate_total_calories(sender, **kwargs):
    if sender == NutritionLogging:
        instance = kwargs['instance']
        nutrition_info = instance.nutrition
        image = instance.meal_image

        carb = int(nutrition_info.carb)
        protein = int(nutrition_info.protein)
        fats = int(nutrition_info.fats)
        total_calories = (carb*4) + (protein*9) + (fats*4)
        MealImage.objects.filter(image_id=image.image_id).update(total_calorie=total_calories)