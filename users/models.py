from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)

    REQUIRED_FIELDS = [email, username]
