from django.shortcuts import render
from .models import *

# Create your views here.

def hme(request):
    if request.method=="POST":
        name = request.POST['username']
        address = request.POST['address']
        phone = request.POST['phn']
        email = request.POST['email']

        e=Form()
        e.name=name
        e.address=address
        e.phone=phone
        e.email=email
        e.save()

    return render(request,"home.html")

def cont(request):

    return render(request,"contact.html")

def Abou(request):

    return render(request,"about.html")

def services(request):
    return  render(request,"sevice.html")

def Path(request):
    return render(request,"path.html")

def TestImgTwo(request):
    return render(request,"imgtwo.html")