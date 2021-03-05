from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
	first_name = forms.CharField(required=True , widget=forms.TextInput(attrs={'placeholder':'First Name..'}))
	last_name = forms.CharField(required=True , widget=forms.TextInput(attrs={'placeholder':'Last Name..'}))
	description = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Description..'}))
	address = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Address..'}))
	website = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Website..'}))
	github = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Github..'}))
	twitter = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Twitter..'}))
	instagram = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Instagram..'}))
	facebook = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Facebook..'}))
	phone = forms.CharField(required=False , widget=forms.TextInput(attrs={'placeholder':'Phone..'}))
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name','phone','email', 'description', 'phone', 'website','github', 'instagram', 'facebook', 'twitter']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = ('first_name', 'last_name','phone','email','profile_pic','city', 'description', 'phone', 'website', 'github', 'instagram', 'facebook', 'twitter')

class EditProfileForm(ModelForm):
        class Meta:
        	model = User
        	fields = ('email', 'first_name', 'last_name')
class ProfileForm(ModelForm):
        class Meta:
         model = Customer
         fields = ('city', 'description', 'phone', 'website', 'profile_pic', 'github', 'instagram', 'facebook', 'twitter')
