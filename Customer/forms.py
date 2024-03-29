from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label='first_name')
    last_name = forms.CharField(label='last_name')
    description = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Description..'}))
    address = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Address..'}))
    website = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Website..'}))
    github = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Github..'}))
    twitter = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Twitter..'}))
    instagram = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Instagram..'}))
    facebook = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Facebook..'}))
    phone = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Phone..'}))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name',
                  'phone', 'email', 'description', 'website', 'github', 'instagram', 'facebook', 'twitter']


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
        fields = ('address', 'description', 'phone', 'website',
                  'profile_pic', 'github', 'instagram', 'facebook', 'twitter')
