from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(LoginRequiredMixin, View):
    template_name = "users/profile.html"

    def get(self, request):
        books = request.user.book_set.all()

        bundle_offers = request.user.bundleoffer_set.all()
        print(bundle_offers)
        single_offers = request.user.singlebookoffer_set.all()
        context = {
            "books": books,
            "bundle_offers": bundle_offers,
            "single_offers": single_offers
        }
        return render(request, self.template_name, context)
