from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile',
                                on_delete=models.CASCADE)

