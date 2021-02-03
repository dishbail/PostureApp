from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'User/main.html')

def notif(request):
    return render(request, 'User/notif.html')

def graph(request):
    return render(request, 'User/graph.html')

def model(request):
    return render(request, 'User/model.html')
