from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.council_list, name='council_list'),
]
