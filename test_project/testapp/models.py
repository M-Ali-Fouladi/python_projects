
from django.contrib.auth.models import AbstractUser
from django.db import models

 
class CustomUser(AbstractUser):

   ROLE_CHOICES={
        ('admin','admin'),
        ('user', 'user'),
        ('guest', 'guest'),
    }
   role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')

class city(models.Model):
    name=models.CharField(max_length=20)
    population=models.FloatField(max_length=5)
    
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
"""

    # Add your custom fields here, for example:
   

    # Add more custom fields as needed

def __str__(self):
    return self.user.username

