from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

USER = get_user_model()


class Profile(LoginRequiredMixin, View):
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
