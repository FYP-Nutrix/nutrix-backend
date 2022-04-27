from urllib.parse import urldefrag
from django.urls import path
from .views import *

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/', UserRecordView.as_view(), name='users'),
]
