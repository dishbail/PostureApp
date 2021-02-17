from django.urls import path
from . import views

app_name = 'Customer'

urlpatterns = [
    path('', views.home, name = "dashboard"),
    path('notifications/', views.notif, name="notifications"),
    path('graphs/', views.graph, name="graph"),
    path('models/', views.model, name="model"),
    path('profile/', views.profile, name="profile"),

    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user_settings/', views.userSettings, name="user_settings"),

    path('getGraphData/', views.getGraphData, name="get_graph_data"),

]
