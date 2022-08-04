from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('meal-image/', MealImageList.as_view(), name='MealImageList'),
    path('meal-image/<uuid:pk>/', MealImageDetails.as_view(), name='MealImageDetails'),
    path('meal-log/', MealLogList.as_view(), name='MealLogList'),
    path('meal-log/<uuid:pk>/', MealLogDetails.as_view(), name='MealLogDetails'),
]

urlpatterns = format_suffix_patterns(urlpatterns)