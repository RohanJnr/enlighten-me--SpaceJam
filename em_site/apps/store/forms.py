from django import forms
from django.forms.widgets import CheckboxSelectMultiple

from .models import Book, BundleOffer, Tag, SingleBookOffer


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ("user",)


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class BundleOfferForm(forms.ModelForm):
    class Meta:
        model = BundleOffer
        exclude = ("user", "buyer")


class SingleBookOfferForm(forms.ModelForm):
    class Meta:
        model = SingleBookOffer
        exclude = ("user", "buyer")
