from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('signIn/', views.SignIn, name='signIn'),
    path('register/',views.Register, name='register'),
    path('dashboard/',views.Dashboard, name='dashboard'),
    path('users/logout/', views.LogoutUser, name='logout'),
]
