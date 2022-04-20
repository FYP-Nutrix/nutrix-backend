from urllib.parse import urldefrag
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
