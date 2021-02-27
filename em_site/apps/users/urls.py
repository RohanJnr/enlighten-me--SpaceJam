from django.urls import path

from .views import Profile, HomeRedirect


urlpatterns = [
    path("", HomeRedirect.as_view(), name="users-home"),
    path("profile/<str:username>", Profile.as_view(), name="users-profile")
]