from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    fullname = models.CharField(max_length=128)
    profile_picture = models.ImageField(upload_to="account-images")
    created = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.username

