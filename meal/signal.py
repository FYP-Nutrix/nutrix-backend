from django.db.models.signals import post_save, pre_save
from meal.models import MealImage, MealLogging
from django.dispatch import receiver

from nutrition.models import Nutrition, NutritionLogging

# receive meal image then put the meal name
# @receiver(post_save, sender=MealImage)
# def add_meal_name(sender, **kwargs):
#     if sender == MealImage:
#         print("this code is running")
#         instance = kwargs['instance']
#         print(type(instance.meal_image))
#     else :
#         print("something is wrong")

@receiver(post_save, sender=MealImage)
def generate_nutrition(sender, **kwargs):
    if sender == MealImage:
        instance = kwargs['instance']
        # use the instance meal name to find the food name in nutrition table
        new_meal_name = instance.meal_name
        try:
            nutrition_info = Nutrition.objects.get(meal_name=new_meal_name)
            print(nutrition_info.fiber)
            # to get back the previous meal information entry
            meal_image_id = instance.image_id
            meal_image_obj = MealImage.objects.get(image_id=meal_image_id)
            meal_calorie = MealImage.objects.filter(image_id=meal_image_id).update(total_calorie=(nutrition_info.calorie_per_serving*meal_image_obj.meal_size))
            data = NutritionLogging(meal_image=meal_image_obj,nutrition=nutrition_info)
            data.save()
        except Nutrition.DoesNotExist:
            print("no data")