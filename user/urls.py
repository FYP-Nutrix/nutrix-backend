from django.urls import path
from .views import *
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', UserList.as_view(), name='UserList'),
    path('user/<uuid:pk>/', views.UserDetails.as_view()),
    path('meal-setting/', views.MealSettingList.as_view(), name='MealSettingList'),
    path('meal-setting/<uuid:pk>/', views.MealSettingDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)