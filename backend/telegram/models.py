from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PhoneNumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12)

    def __str__(self):
        return self.phone_number
