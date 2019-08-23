from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    biography = models.CharField(max_length=255)
    profile_image = models.ImageField(upload_to="profile_images")
