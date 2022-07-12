from django.contrib import admin

from nutrition.models import Nutrition, NutritionLogging

# Register your models here.
admin.site.register(Nutrition)
admin.site.register(NutritionLogging)