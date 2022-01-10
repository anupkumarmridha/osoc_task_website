from django.db import models
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from datetime import datetime
#import re
from home.models import Contact

# Create your views here.
def home(request):
    return render(request,'home/home.html')
def teams(request):
    return render(request,'home/teams.html')
def contact(request):
    return render(request,'home/contact.html')
def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(desc)<4:
            messages.error(request, "Please fill the from correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc, timeStamp=datetime.today())
            contact.save()
            messages.success(request, 'Your Massage has been sent!.')
    return render(request, 'home/contact.html')


