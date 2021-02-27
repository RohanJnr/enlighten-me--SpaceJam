from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BookForm, SingleBookOfferForm, BundleOfferForm


class AddBook(LoginRequiredMixin, View):
    template_name = "store/add_book.html"

    def get(self, request):
        form = BookForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("users-profile")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class CreateSingleBookOffer(LoginRequiredMixin, View):
    template_name = "store/create_single_offer.html"

    def get(self, request):
        form = SingleBookOfferForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SingleBookOfferForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("users-profile")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class CreateBundleOffer(LoginRequiredMixin, View):
    template_name = "store/create_bundle_offer.html"

    def get(self, request):
        form = BundleOfferForm()
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = BundleOfferForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect("users-profile")
        context = {
            "form": form
        }
        return render(request, self.template_name, context)
