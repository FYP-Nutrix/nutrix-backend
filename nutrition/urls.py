from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('nutrition/', NutritionList.as_view(), name='NutritionList'),
    path('nutrition/<uuid:pk>/', NutritionDetails.as_view(), name='NutritionDetails'),
    path('nutrition-log/', NutritionLogList.as_view(), name='NutritionLogList'),
    path('nutrition-log/<uuid:pk>/',NutritionLogDetails.as_view(),name='NutritionLogDetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)