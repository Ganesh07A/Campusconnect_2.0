import openpyxl  #for downloading all registrations
from django.http import HttpResponse

from django.shortcuts import render, redirect, get_object_or_404
from .models import Event, EventRegistration
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url='signIn')
def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/events_list.html', {'events': events})

def register_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        year = request.POST.get('year')
        EventRegistration.objects.create(event=event, name=name, email=email, year=year)
    # or use a success message
        messages.success(request, "Thank you! you've been registered successfully")
        return redirect('event_list')  
    

def export_registrations_excel(request) :
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = 'Registrations'

    #header rows namings
    headers = ['Event Title', 'Name', 'Email', 'Year', 'Registered On']
    sheet.append(headers)

    # Data rows
    registrations = EventRegistration.objects.select_related('event').all()
    for reg in registrations:
        sheet.append([
            reg.event.title,
            reg.name,
            reg.email,
            reg.year,
            reg.created_at.strftime("%Y-%m-%d %H:%M:%S") if hasattr(reg, 'created_at') else '',
        ])


    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',) 
    response['Content-Disposition'] = 'attachment; filename=event_registrations.xlsx'
    workbook.save(response)
    return response