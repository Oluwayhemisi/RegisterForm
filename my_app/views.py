from django.shortcuts import render, redirect, HttpResponse
from django.conf import settings
from .models import Contact


# Create your views here.

def index(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        if firstname and lastname and password:
            contact = Contact(firstname=firstname, lastname=lastname, password=password, email=email)
            contact.save()
        else:
            return HttpResponse(f'1{firstname} 2{lastname} 3{password} 4{email}')
    return render(request, 'index.html')
