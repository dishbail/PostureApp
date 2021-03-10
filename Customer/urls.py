from django.urls import path
from . import views

app_name = 'Customer'

urlpatterns = [
    path('', views.home, name = "home"),
    path('notifications/', views.notif, name="notifications"),
    path('graphs/', views.graph, name="graph"),
    path('models/', views.model, name="model"),
    path('profile/', views.profile, name="profile"),
    path('edit_profile/',views.edit_profile, name="edit_profile"),
    path('edit_picture/',views.edit_picture, name="edit_picture"),

    path('register/', views.register, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('getGraphData/', views.getGraphData, name="get_graph_data"),

]
