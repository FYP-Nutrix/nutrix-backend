from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.CreateFoodTypeView.as_view(), name="foodType"),
    path("viewLabelFood/", views.ViewFoodLabel.as_view(), name="viewLabelFood"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)