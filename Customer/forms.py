from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class CreateUserForm(UserCreationForm):
	#first_name = forms.CharField(required=True , widget=forms.TextInput(attrs={'placeholder':'First Name..'}))
	#last_name = forms.CharField(required=True , widget=forms.TextInput(attrs={'placeholder':'Last Name..'}))
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
		fields = ['username', 'email', 'password1', 'password2','phone','email', 'description', 'website','github', 'instagram', 'facebook', 'twitter']

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'

class EditProfileForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ('user',)
class EditUserForm(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		exclude = ('user',)
class ProfileForm(ModelForm):
        class Meta:
         model = Customer
         fields = ('address', 'description', 'phone', 'website', 'profile_pic', 'github', 'instagram', 'facebook', 'twitter')
