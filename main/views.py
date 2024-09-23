from django.shortcuts import render
from .models import Link, TeamMember, Page, BlogPost, Offer
from .forms import ContactForm, MembershipForm
from django. conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError

import datetime

# Create your views here.
year = datetime.datetime.now().year

def home(request):
    page = Page.objects.get(page='home')
    offers = Offer.objects.filter(frontpage=True)
    return render(request, 'home.html', {'page': page, 'year': year, 'offers': offers})

def about(request):
    advisors = TeamMember.objects.filter(team='advice')
    vorstand = TeamMember.objects.filter(team='vorstand')
    page = Page.objects.get(page='about')
    return render(request, 'about.html', {'page': page, 'year': year, 'advisors': advisors, 'vorstand': vorstand})

def offer(request):
    page = Page.objects.get(page='offer')
    offers = Offer.objects.all()
    return render(request, 'offer.html', {'page': page, 'year': year, 'offers': offers})

def contact(request):
    page = Page.objects.get(page='contact')
    submitted = False
    email_error = False
    
    form = ContactForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        cd = form.cleaned_data
        subject, from_email = 'Mitgliederanmeldung Patientenstelle', settings.EMAIL_HOST_USER
        data = {
            'salutation': cd['salutation'], 
            'prename': cd['prename'], 
            'name': cd['name'], 
            'email': cd['email'], 
            'phone': cd['phone'], 
            'street': cd['street'], 
            'plz': cd['plz'], 
            'place': cd['place'], 
            'message': cd['message'], 
            'membership': membership
        }

        customer_html_content = render_to_string('email-membership-customer.html', data)
        admin_html_content = render_to_string('email-membership-admin.html', data)
        customer_text_content = render_to_string('email-membership-customer.txt', data)
        admin_text_content = render_to_string('email-membership-admin.txt', data)

        try:
            customer_msg = EmailMultiAlternatives(subject, customer_text_content, from_email, [cd['email']])
            customer_msg.attach_alternative(customer_html_content, "text/html")
            customer_msg.send()

            admin_msg = EmailMultiAlternatives(subject, admin_text_content, from_email, ['patientenstelle.basel@bluewin.ch'])
            admin_msg.attach_alternative(admin_html_content, "text/html")
            admin_msg.send()
        except Exception as e:
            return HttpResponseRedirect('?email_error=True')

        return HttpResponseRedirect('?submitted=True')
    else:
        form = MembershipForm(request.POST or None)
        if 'submitted' in request.GET:
            submitted = True
        elif 'email_error' in request.GET:
            email_error = True

    return render(request, 'contact.html', {'page': page, 'year': year, 'form': form,'submitted': submitted, 'email_error': email_error})

def membership(request):
    page = Page.objects.get(page='membership')
    return render(request, 'membership.html', {'page': page, 'year': year})

def membership_form(request, slug):
    submitted = False
    email_error = False
    page = Page.objects.get(page='membership')
    form = MembershipForm(request.POST or None)
    if slug == 'single':
        membership = 'Anmeldung Einzelmitgliedschaft'
    elif slug == 'patron':
        membership = 'Gönner*in werden'
    elif slug == 'family':
        membership = 'Anmeldung Familienmitgliedschaft'
    if request.method == 'POST' and form.is_valid():
        try:
            cd = form.cleaned_data
            subject, from_email = 'Mitgliederanmeldung Patientenstelle', settings.EMAIL_HOST_USER
            data = {'salutation':cd['salutation'], 'prename': cd['prename'], 'name': cd['name'], 'email':cd['email'], 'phone':cd['phone'], 'street':cd['street'], 'plz':cd['plz'], 'place':cd['place'], 'message':cd['message'], 'membership': membership}
            customer_html_content = render_to_string('email-membership-customer.html', data)
            admin_html_content = render_to_string('email-membership-admin.html', data)
            customer_text_content = render_to_string('email-membership-customer.txt', data)
            admin_text_content = render_to_string('email-membership-admin.txt', data)
            customer_msg = EmailMultiAlternatives(subject, customer_text_content, from_email, [cd['email']])
            customer_msg.attach_alternative(customer_html_content, "text/html")
            customer_msg.send()
            admin_msg = EmailMultiAlternatives(subject, admin_text_content, from_email, ['patientenstelle.basel@bluewin.ch'])
            admin_msg.attach_alternative(admin_html_content, "text/html")
            admin_msg.send()
        except Exception as e:
            return HttpResponseRedirect('?email_error=True')

        return HttpResponseRedirect('?submitted=True')
    else:
        form = MembershipForm(request.POST or None)
        if 'submitted' in request.GET:
            submitted = True
        elif 'email_error' in request.GET:
            email_error = True

    return render(request,'membership-form.html', {'form': form, 'page': page, 'year': year, 'membership': membership, 'submitted': submitted, 'email_error': email_error})

def news(request):
    page = Page.objects.get(page='news')
    posts = BlogPost.objects.filter(published = True).order_by('-date')
    return render(request, 'news.html', {'page': page, 'year': year, 'posts': posts})

def single_post(request, pk):
    post = BlogPost.objects.get(pk=pk)
    page = Page.objects.get(page='news')
    return render(request, 'single-post.html', {'post': post, 'page': page, 'year': year})

def links(request):
    page = Page.objects.get(page='links')
    links = Link.objects.all()
    return render(request, 'links.html', {'page': page, 'year': year, 'links': links})

def agb(request):
    page = Page.objects.get(page='agb')
    return render(request, 'legal.html', {'page': page, 'year': year})

def privacy(request):
    page = Page.objects.get(page='privacy')
    return render(request, 'legal.html', {'page': page, 'year': year})

def impressum(request):
    page = Page.objects.get(page='impressum')
    return render(request, 'legal.html', {'page': page, 'year': year})