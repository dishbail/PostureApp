from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import django

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
from background_task import background
from django.contrib import messages

import json
import serial
import numpy as np
import pickle
import random,time

def call_once():
    filename = './static/model/SVM.sav'
    model = pickle.load(open(filename, 'rb'))

def readdata():
    ser = serial.Serial('COM3',9600)
    x = np.ones(256)
    y = ser.readline().decode('UTF-8').split(", ")
    ser.close()
    if len(y) !=256:
        y = readdata()
    x = np.array(y)
    x = x.astype(np.float)
    if x.ndim<2:
        x = x[np.newaxis,...]
    return x

@login_required(login_url='Customer:login')
def home(request):
    #runAlgo(user.id, repeat=60)
    #messages.add_message(request, messages.INFO, value)
    return render(request, 'Customer/dashboard.html')

@login_required(login_url='Customer:login')
def notif(request):
    return render(request, 'Customer/notif.html')

@login_required(login_url='Customer:login')
def notifsAjax(request):
    return render(request, 'Customer/notifajax.html')

@login_required(login_url='Customer:login')
def getNotifData(request):
    customer = request.user.customer
    records = customer.posturerecord_set.all()
    records = records.order_by('-date_created')
    data = []
    for r in records:
        data.append({'Date': r.date_created.strftime("%Y-%m-%d %H:%M:%S"), 'Posture': r.get_posture_value_display()})
    return JsonResponse({'data':data})

@login_required(login_url='Customer:login')
def notifications(request):
    #runAlgo(request.user.id, repeat=60)
    runAlgo2(request)
    customer = request.user.customer
    records = customer.posturerecord_set.all()
    records = records.order_by('-date_created')
    return render(request, 'Customer/notifications.html',{'records':records})

@login_required(login_url='Customer:login')
def graph(request):
    return render(request, 'Customer/graph.html')

@login_required(login_url='Customer:login')
def model(request):
    return render(request, 'Customer/model.html')

@login_required(login_url='Customer:login')
def profile(request):
    return render(request, 'Customer/profile.html')

@background(schedule=0) #how long after function is called should it execute
def runAlgo(user_id):
    user = User.objects.get(pk=user_id)
    customer = user.customer
    x = readdata()
    data = model.predict(x)
    if(data == 0):
        result = 1
    else:
        result = 0
    PostureRecord.objects.create(customer=customer, posture_value=result)

def runAlgo2(request):
    customer = request.user.customer
    x = readdata()
    print(x)
    filename = 'Customer\static\model\SVM.sav'
    svm_model = pickle.load(open(filename, 'rb'))
    data = svm_model.predict(x)
    now = django.utils.timezone.now()
    if(data == 0):
        result = 1
    else:
        result = 0
    PostureRecord.objects.create(customer=customer, date_created = now, posture_value=result)
@login_required(login_url='Customer:login')
def getGraphData(request):
    customer = request.user.customer
    #posture_database = customer.posturerecord_set.all()
    posture_database = PostureRecord.objects.filter(customer=customer)
    sitting_database = customer.sittingrecord_set.all()
    posture_data = []
    sitting_data = []
    for i in posture_database:
        posture_data.append([i.date_created.timestamp()*1000, i.get_posture_value_display()])
    for i in sitting_database:
        sitting_data.append([i.date_created.timestamp()*1000, i.sitting_time_in_min])
    return JsonResponse({'customer':customer.user.username,'posture_data': posture_data, 'sitting_data':sitting_data})

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            instance = form.cleaned_data
            Customer.objects.create(
                user=user,
                phone = instance.get('phone'),
                description = instance.get('description'),
                address = instance.get('address'),
                website = instance.get('website'),
                github = instance.get('github'),
                twitter = instance.get('twitter'),
                instagram = instance.get('instagram'),
                facebook = instance.get('facebook')
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

@login_required
def edit_picture(request):
    return redirect('/')
@login_required
def edit_profile(request):
    user = request.user
    customer = user.customer
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, request.FILES,instance=customer)
        user_form = EditUserForm(request.POST, request.FILES,instance=user)
        #profile_form = ProfileForm(request.POST, request.FILES, instance=request.user)  # request.FILES is show the selected image or file
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User Information Updated')
            user.refresh_from_db()

        if profile_form.is_valid():
            #custom_form = profile_form.save(False)
            profile_form.user = user
            profile_form.save()
            customer.refresh_from_db()
            messages.success(request, 'Profile Information Updated')
            return redirect('/profile')
        else:
            return redirect('/')
    else:
        profile_form = EditProfileForm(instance=customer)
        user_form = EditUserForm(instance=user)
        #form = EditProfileForm(instance=customer)
        #profile_form = ProfileForm(instance=request.user)
        #args = {}
        #args.update(csrf(request))
        #args['form'] = form
        #args['profile_form'] = profile_form
        context = {'user_form':user_form, 'profile_form':profile_form, 'customer': customer}
        return render(request, 'Customer/edit_profile.html', context)
