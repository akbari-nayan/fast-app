from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class CustomUser(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_service_provider = models.BooleanField(default=False)