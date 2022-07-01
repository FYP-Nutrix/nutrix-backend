from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('nutrition/', NutritionList.as_view(), name='NutritionList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)