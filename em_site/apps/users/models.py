from django.contrib.auth import get_user_model
from django.db import models

USER = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(USER, on_delete=models.CASCADE, default=1)
    fullname = models.CharField(max_length=256)
    phone = models.PositiveBigIntegerField()
    address = models.CharField(max_length=512)
    city = models.CharField(choices=[("Bangalore", "Bangalore")], default="Bangalore", max_length=256)
    pincode = models.PositiveBigIntegerField()

    def __str__(self):
        return self.fullname
