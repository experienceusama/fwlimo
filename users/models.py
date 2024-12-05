from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    # Removing the username field
    username = None  
    
    mobile_number = PhoneNumberField(blank=False, null=False, unique=True)
    email = models.EmailField(blank=True, null=True, unique=True)

    USERNAME_FIELD = 'mobile_number'  # Mobile number as the identifier
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return self.mobile_number.as_e164
