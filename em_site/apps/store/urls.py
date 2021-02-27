from django.urls import path

from .views import (
    AddBook,
    CreateSingleBookOffer,
    create_bundle_offer,
    DeleteSingleOffer,
    EditSingleBookOffer,
    DeleteBundleOffer,
    EditBundleOffer,
    SingleOfferDetail,
    BundleOfferDetail
)


urlpatterns = [
    path("add-book", AddBook.as_view(), name="store-add-book"),
    path("create-offer/single", CreateSingleBookOffer.as_view(), name="store-single-offer"),
    path("create-offer/bundle", create_bundle_offer, name="store-bundle-offer"),

    path("delete-offer/single/<int:pk>", DeleteSingleOffer.as_view(), name="store-delete-single"),
    path("edit-offer/single/<int:pk>", EditSingleBookOffer.as_view(), name="store-edit-single"),
    path("detail-offer/single/<int:pk>", SingleOfferDetail.as_view(), name="store-detail-single"),

    path("delete-offer/bundle/<int:pk>", DeleteBundleOffer.as_view(), name="store-delete-bundle"),
    path("edit-offer/bundle/<int:pk>", EditBundleOffer.as_view(), name="store-edit-bundle"),
    path("detail-offer/bundle/<int:pk>", BundleOfferDetail.as_view(), name="store-detail-bundle"),


]
