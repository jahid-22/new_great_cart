from django.db import models

# Create your models here.

class Country (models.Model):
    name            = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
    

# models.py
from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')])
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
