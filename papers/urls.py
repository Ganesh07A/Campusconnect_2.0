from django.urls import path
from . import views

urlpatterns = [
    path('pyqs/',views.Pre_years_papers, name= 'pyqs')
]
