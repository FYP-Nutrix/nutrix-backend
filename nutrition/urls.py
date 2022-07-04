from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('nutrition/', NutritionList.as_view(), name='NutritionList'),
    path('nutrition/<uuid:pk>/', NutritionDetails.as_view(), name='NutritionDetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)