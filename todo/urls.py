from django.urls import path
from . import views


urlpatterns = [
    #--------HOME PAGE--------------

    path('', views.home, name=""),

    #---------REGISTER---------------

    path('register', views.register, name='register'),

    #---------LOGIN----------------

    path('login', views.my_login, name="my-login"),

    #---------DASHBOARD----------------

    path('dashboard', views.dashboard, name="dashboard"),

    #---------LOGOUT----------------
    path('user-logout', views.user_logout, name="user-logout"),


]