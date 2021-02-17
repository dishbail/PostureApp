from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    #customer = request.user.customer
    #posture_data = customer.posturerecord_set.all()
    #sitting_data = customer.sittingrecord_set.all()
    posture_dates = []
    posture_values = []
    sitting_dates = []
    sitting_values = []
    #for i in posture_data:
        #posture_dates.append(i.date_created)
        #posture_values.append(i.posture_value)
    #for i in sitting_data:
        #sitting_dates.append(i.date_created)
        #sitting_values.append(i.sitting_time_in_min)
    posture_dates = ["monday", "tuesday"]
    posture_values = [2,3]
    sitting_dates = ["wednesday", "tuesday"]
    sitting_values = [4,5]
    return JsonResponse({'posture_dates': posture_dates, 'posture_values':posture_values, 'sitting_dates':sitting_dates, 'sitting_values':sitting_values})

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
