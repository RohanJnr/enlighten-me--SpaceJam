from rest_framework import serializers

from .models import BundleOffer


class BundleOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BundleOffer
        fields = ("books", "user", "price")

        read_only_fields = ("user",)
