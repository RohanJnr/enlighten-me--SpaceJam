from django.urls import path

from .views import ProfileView, HomeRedirect, Register


urlpatterns = [
    path("", HomeRedirect.as_view(), name="users-home"),
    path("profile/<str:username>", ProfileView.as_view(), name="users-profile"),
    path("register", Register.as_view(), name='users-register')
]