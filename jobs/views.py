from django.shortcuts import render
from .models import job

# Create your views here.

def homepage(request):
    jobs = job.objects
    return render(request, 'jobs/home.html', {'jobs':jobs})

def contact(request):
    return render(request, 'jobs/contact.html')

def resume(request):
    return render(request, 'jobs/resume.html')