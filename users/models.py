from distutils.command.upload import upload
from re import U
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="user.jpg", upload_to="PROFILE_PICS")

    def __str__(self):
        return f"{self.user.username} Profile"
