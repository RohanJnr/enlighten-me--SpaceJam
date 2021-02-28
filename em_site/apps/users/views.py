from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile

USER = get_user_model()


class ProfileView(LoginRequiredMixin, View):
    template_name = "users/profile.html"

    def get(self, request, username):
        user = get_object_or_404(USER, username=username)
        bundle_offers = user.bundleoffer_set.all()
        single_offers = user.singlebookoffer_set.all()
        context = {
            "username": username,
            "bundle_offers": bundle_offers,
            "single_offers": single_offers
        }
        return render(request, self.template_name, context)


class HomeRedirect(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("users-profile", username=request.user.username)
        return redirect("users-login")


class Register(View):
    template_name = "users/register.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("users-profile", username=request.user.username)
        return render(request, self.template_name)

    def post(self, request):
        p = request.POST
        user = User.objects.create_user(
            username=p.get("username"),
            password=p.get("password"),
            email=p.get("email")
        )
        Profile.objects.create(
            user=user,
            fullname=p.get("fullname"),
            address=p.get("address"),
            city=p.get("city"),
            phone=p.get("phone"),
            pincode=p.get("pincode"),
        )
        return redirect("users-profile", username=user.username)


class Login(View):
    template_name = "users/signin.html"

    def get(self, request):
        if request.user.is_authenticated:
            return redirect("users-profile", username=request.user.username)
        return render(request, self.template_name)

    def post(self, request):
        user = authenticate(
            username=request.POST.get("username"),
            password=request.POST.get("password")
        )
        login(request, user)
        return redirect("users-profile", username=user.username)
