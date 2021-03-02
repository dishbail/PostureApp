from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    website = models.URLField(default='')
    github = models.URLField(default='')
    twitter = models.URLField(default='')
    instagram = models.URLField(default='') 
    facebook = models.URLField(default='')
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __str__(self):
        return self.user.username

class PostureRecord(models.Model):
    POSTURE_CHOICES = (
        (1, 'Correct Posture'),
        (0, 'Incorrect Posture')
    )
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    posture_value = models.CharField(choices = POSTURE_CHOICES, max_length = 30, null = True)
    confidence_value = models.FloatField(default = 1)

class SittingRecord(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    sitting_time_in_min = models.FloatField(default = 0)
