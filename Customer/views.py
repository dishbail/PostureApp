from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import *
from.models import *
from .decorators import *
from datetime import timezone

@login_required(login_url='Customer:login')
def home(request):
    return render(request, 'Customer/dashboard.html')

@login_required(login_url='Customer:login')
def notif(request):
    return render(request, 'Customer/notif.html')

@login_required(login_url='Customer:login')
def graph(request):
    return render(request, 'Customer/graph.html')

@login_required(login_url='Customer:login')
def model(request):
    return render(request, 'Customer/model.html')

@login_required(login_url='Customer:login')
def profile(request):
    return render(request, 'Customer/profile.html')

def getGraphData(request):
    customer = request.user.customer
    posture_database = customer.posturerecord_set.all()
    sitting_database = customer.sittingrecord_set.all()
    posture_data = []
    sitting_data = []
    for i in posture_database:
        posture_data.append([i.date_created, i.posture_value])
    for i in sitting_database:
        sitting_data.append([i.date_created, i.sitting_time_in_min])
    posture_data = []
    sitting_data = []
    return JsonResponse({'posture_data': posture_data, 'sitting_data':sitting_data})

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            Customer.objects.create(
                user=user,name = user.username, phone = None, email = user.email
            )
            messages.success(request, 'Account was created for ' + user.username)
            return redirect('/login')
    context = {'form':form}
    return render(request, 'Customer/register.html', context)

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'Customer/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='Customer:login')
def userSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'Customer/user_settings.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)  # request.FILES is show the selected image or file
        if form.is_valid() and profile_form.is_valid():
            user_form = form.save()
            custom_form = profile_form.save(False)
            custom_form.user = user_form
            custom_form.save()
            return redirect('Customer/profile.html')
    else:
        form = EditProfileForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user)
        args = {}
        #args.update(csrf(request))
        args['form'] = form
        args['profile_form'] = profile_form
        return render(request, 'Customer/edit_profile.html', args)
