from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    description = models.CharField(max_length=255, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_image", null=True, blank=True)
