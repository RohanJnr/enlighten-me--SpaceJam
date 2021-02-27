from django.urls import path

from .views import AddBook, CreateSingleBookOffer, CreateBundleOffer, DeleteSingleOffer, EditSingleBookOffer


urlpatterns = [
    path("add-book", AddBook.as_view(), name="store-add-book"),
    path("create-offer/single", CreateSingleBookOffer.as_view(), name="store-single-offer"),
    path("create-offer/bundle", CreateBundleOffer.as_view(), name="store-bundle-offer"),
    path("delete-offer/single/<int:pk>", DeleteSingleOffer.as_view(), name="store-delete-single"),
    path("edit-offer/single/<int:pk>", EditSingleBookOffer.as_view(), name="store-edit-single"),
]
