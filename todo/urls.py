from django.urls import path
from . import views


urlpatterns = [

    path('register', views.register),

    path('my-login', views.my_login),

    path('', views.home, name=""),


    #---------CRUD operations-------
    #create
    path('create-task', views.createTask, name='create-task'),

    #read
    path('view-tasks', views.viewTasks, name='view-tasks'),

    #update 
    path('update-task/<str:pk>/', views.updateTask, name='update-task'),

    #delete 
    path('delete-task/<str:pk>/', views.deleteTask, name='delete-task'),

    #---------REGISTER---------------

    path('register', views.register, name='register'),

    #---------LOGIN----------------

    path('login', views.my_login, name="my-login"),

    #---------DASHBOARD----------------

    path('dashboard', views.dashboard, name="dashboard"),

    #---------LOGOUT----------------
    path('user-logout', views.user_logout, name="user-logout"),


]