from django.shortcuts import render
from .models import Council
from django.contrib.auth.decorators import login_required

@login_required(login_url='signIn')
def council_list(request):
    members = Council.objects.all()
    return render(request, 'council/list.html', {'members': members})
