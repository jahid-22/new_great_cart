from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .custom_user_manager import CustomUserManager


# Create your models here.

class Country (models.Model):
    name            = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    
# Custom User Model 
class Person(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, unique=True)
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')])
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    
    # Fields from AbstractBaseUser
    is_staff = models.BooleanField(default=False)  # required for staff status
    is_superuser = models.BooleanField(default=False)  # required for superuser status
    last_login = models.DateTimeField(null=True, blank=True)  # required for last login


    # Use the custom user manager for this model
    objects = CustomUserManager()

    # The field that will be used for authentication (login)
    USERNAME_FIELD = "email"

    # Additional fields required to be provided when creating a user (other than username and password)
    REQUIRED_FIELDS = []
