from django.shortcuts import render
from .models import Link, Newsletter, TeamMember, Page

# Create your views here.

def home(request):
    page = 'home'
    return render(request, 'home.html', {'page': page})

def about(request):
    team = TeamMember.objects.all()
    page = 'about'
    return render(request, 'about.html', {'team': team, 'page': page})