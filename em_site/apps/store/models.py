from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_delete, post_save

from .signals import delete_book_image, resize_book_image


USER = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Book(models.Model):
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    image = models.ImageField(upload_to="books")
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return f"{self.name}"


class BundleOffer(models.Model):
    title = models.CharField(max_length=256, default="A bundle of books.")
    books = models.ManyToManyField(Book)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    buyer = models.ForeignKey(
        USER,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="bundle_offer_buyer"
    )

    def __str__(self):
        return f"{len(self.books.all())} - {self.price}"


class SingleBookOffer(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(USER, on_delete=models.CASCADE)
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )
    buyer = models.ForeignKey(
        USER,
        on_delete=models.SET_NULL,
        default=None,
        null=True,
        blank=True,
        related_name="single_offer_buyer"
    )

    def __str__(self):
        return f"{self.book} - {self.price}"


post_delete.connect(delete_book_image, sender=Book)
post_save.connect(resize_book_image, sender=Book)
