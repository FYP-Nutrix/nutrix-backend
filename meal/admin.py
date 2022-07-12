from django.contrib import admin

from meal.models import MealImage, MealLogging

# Register your models here.
admin.site.register(MealLogging)
admin.site.register(MealImage)