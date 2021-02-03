from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), blank=True, null=True)

    def __str__(self):
        return self.user.username
