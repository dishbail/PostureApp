from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True, blank= True)
    description = models.CharField(max_length=200, default='',blank= True)
    address = models.CharField(max_length=200, default='', blank= True)
    website = models.URLField(default='', null=True, blank= True)
    github = models.URLField(default='', null=True, blank= True)
    twitter = models.URLField(default='', null=True, blank= True)
    instagram = models.URLField(default='', null=True, blank= True)
    facebook = models.URLField(default='', null=True, blank= True)
    profile_pic = models.ImageField(default="profile1.png")

    def __str__(self):
        return self.user.username

class PostureRecord(models.Model):
    POSTURE_CHOICES = (
        (0, 'Correct Posture'),
        (1, 'Incorrect Posture')
    )
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    posture_value = models.IntegerField(choices = POSTURE_CHOICES, max_length = 30, null = True)
    confidence_value = models.FloatField(default = 1)

class SittingRecord(models.Model):
    customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(default=timezone.now(),blank=True, null=True)
    sitting_time_in_min = models.FloatField(default = 0)
