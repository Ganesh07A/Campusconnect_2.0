from django.shortcuts import render
from .models import Paper
from django.contrib.auth.decorators import login_required


@login_required(login_url='signIn')
def Pre_years_papers(request):
    year_filter = request.GET.get('year')  # this will be '1st', '2nd', etc.

    if year_filter:
        papers = Paper.objects.filter(paper_type=year_filter)
    else:
        papers = Paper.objects.all()

    return render(request, 'PYQS/papers.html', {
        'papers': papers,
    })
