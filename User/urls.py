from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notifications/', views.notif),
    path('graphs/', views.graph),
    path('models/', views.model),


]