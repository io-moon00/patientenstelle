from django.shortcuts import render
from .models import Link, TeamMember, Page, BlogPost

import datetime

# Create your views here.
year = datetime.datetime.now().year

def home(request):
    page = 'home'
    return render(request, 'home.html', {'page': page, 'year': year})

def about(request):
    team = TeamMember.objects.all()
    page = 'about'
    return render(request, 'about.html', {'team': team, 'page': page, 'year': year})

def offer(request):
    page = 'offer'
    return render(request, 'offer.html', {'page': page, 'year': year})

def contact(request):
    page = 'contact'
    return render(request, 'contact.html', {'page': page, 'year': year})

def membership(request):
    page = 'membership'
    return render(request, 'membership.html', {'page': page, 'year': year})

def current(request):
    page = 'current'
    posts = BlogPost.objects.filter(published = True).order_by('-date')
    return render(request, 'current.html', {'page': page, 'year': year, 'posts': posts})