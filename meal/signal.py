from django.db.models.signals import post_save, pre_save
from meal.models import MealImage, MealLogging
from django.dispatch import receiver

# receive meal image then put the meal name
@receiver(post_save, sender=MealImage)
def add_meal_name(sender, **kwargs):
    if sender == MealImage:
        print("this code is running")
        instance = kwargs['instance']
        print(type(instance.meal_image))
    else :
        print("something is wrong")