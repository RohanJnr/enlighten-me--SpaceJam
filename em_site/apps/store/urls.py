from django.urls import path

from .views import AddBook, CreateSingleBookOffer, CreateBundleOffer


urlpatterns = [
    path("add-book", AddBook.as_view(), name="store-add-book"),
    path("create-offer/single", CreateSingleBookOffer.as_view(), name="store-single-offer"),
    path("create-offer/bundle", CreateBundleOffer.as_view(), name="store-bundle-offer")
]
