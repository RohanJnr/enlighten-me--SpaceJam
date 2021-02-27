from django.urls import path

from .views import BundleOfferAPIView


urlpatterns = [
    path("api/bundle", BundleOfferAPIView.as_view()),
]