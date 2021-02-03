from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('notifications/', views.notif),
    path('graphs/', views.graph),
    path('models/', views.model),

    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_settings/', views.userSettings, name="user_settings"),

]
