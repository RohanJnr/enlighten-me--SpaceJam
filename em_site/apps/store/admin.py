from django.contrib import admin

from .models import Book, BundleOffer, Tag, SingleBookOffer


admin.site.register(Book)
admin.site.register(BundleOffer)
admin.site.register(Tag)
admin.site.register(SingleBookOffer)
