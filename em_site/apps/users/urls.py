from django.urls import path

from .views import Profile


urlpatterns = [
    path("profile/<str:username>", Profile.as_view(), name="users-profile")
]