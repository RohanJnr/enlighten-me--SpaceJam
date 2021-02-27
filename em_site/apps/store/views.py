from django import forms
from django.forms.widgets import CheckboxSelectMultiple
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BookForm, SingleBookOfferForm, BundleOfferForm
from .models import Book, SingleBookOffer, BundleOffer


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
            return redirect("users-profile", username=request.user.username)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


# class CreateBundleOffer(LoginRequiredMixin, View):
#     template_name = "store/create_bundle_offer.html"
#
#     def get(self, request):
#         form = BundleOfferForm()
#         context = {
#             "form": form
#         }
#         return render(request, self.template_name, context)
#
#     def post(self, request):
#         form = BundleOfferForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             return redirect("users-profile", username=request.user.username)
#         context = {
#             "form": form
#         }
#         return render(request, self.template_name, context)

@login_required
def create_bundle_offer(request):
    template_name = "store/create_bundle_offer.html"

    class BundleOfferFormTwo(forms.ModelForm):
        class Meta:
            model = BundleOffer
            exclude = ("user", "buyer")

        def __init__(self, *args, **kwargs):
            super(BundleOfferFormTwo, self).__init__(*args, **kwargs)

            self.fields["books"].widget = CheckboxSelectMultiple()
            self.fields["books"].queryset = Book.objects.filter(user=request.user)

    form = BundleOfferFormTwo()
    if request.method == "POST":
        form = BundleOfferFormTwo(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            form.save_m2m()
            return redirect("users-profile", username=request.user.username)
    context = {
        "form": form
    }

    return render(request, template_name, context)


class DeleteSingleOffer(LoginRequiredMixin, View):
    template_name = "store/delete_single_offer.html"

    def get(self, request, pk):
        offer = get_object_or_404(SingleBookOffer, pk=pk)
        context = {
            "offer": offer
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        offer = get_object_or_404(SingleBookOffer, pk=pk)
        offer.delete()
        return redirect("users-profile", username=request.user.username)


class EditSingleBookOffer(LoginRequiredMixin, View):
    template_name = "store/edit_single_offer.html"

    def get(self, request, pk):
        offer = get_object_or_404(SingleBookOffer, pk=pk)
        form = SingleBookOfferForm(instance=offer)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        offer = get_object_or_404(SingleBookOffer, pk=pk)
        form = SingleBookOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect("users-profile", username=request.user.username)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class DeleteBundleOffer(LoginRequiredMixin, View):
    template_name = "store/delete_bundle_offer.html"

    def get(self, request, pk):
        offer = get_object_or_404(BundleOffer, pk=pk)
        context = {
            "offer": offer
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        offer = get_object_or_404(BundleOffer, pk=pk)
        offer.delete()
        return redirect("users-profile", username=request.user.username)


class EditBundleOffer(LoginRequiredMixin, View):
    template_name = "store/edit_bundle_offer.html"

    def get(self, request, pk):
        offer = get_object_or_404(BundleOffer, pk=pk)
        form = BundleOfferForm(instance=offer)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, pk):
        offer = get_object_or_404(BundleOffer, pk=pk)
        form = BundleOfferForm(request.POST, instance=offer)
        if form.is_valid():
            form.save()
            return redirect("users-profile", username=request.user.username)
        context = {
            "form": form
        }
        return render(request, self.template_name, context)


class SingleOfferDetail(DetailView):
    queryset = SingleBookOffer.objects.all()
    template_name = "store/detail_single_offer.html"


class BundleOfferDetail(DetailView):
    queryset = BundleOffer.objects.all()
    template_name = "store/detail_bundle_offer.html"