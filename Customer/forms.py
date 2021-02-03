from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('name','phone','email','profile_pic')
