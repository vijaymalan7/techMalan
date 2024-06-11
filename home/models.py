from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class TeamMember(models.Model):
    link = models.URLField(max_length=200)
    image = models.ImageField(upload_to='team_images/')
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class UserProfile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=128)

class Internship(models.Model):
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='internships/')
    link = models.CharField( max_length=255)
    

