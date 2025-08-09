from django.urls import path
from . import views

urlpatterns = [

   
    path('events_list/', views.event_list, name='event_list'),
    path('eventsList/register/<int:event_id>/',views.register_event,name='register_event'),
    path('export/', views.export_registrations_excel, name='export_registrations'),
]