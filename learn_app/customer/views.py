from django.shortcuts import render
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings
# Create your views here.


def getmaster(request):
    return render(request,"customer/master1.html")
    
def getcustomerhomepage(request):
    return render(request,"customer/homepage1.html")

def getcustomersignup(request):
    msg=""
    if request.method=='POST':
        user_type=request.POST['usertype']
        if user_type=='customer':
            c_firstname=request.POST['_firstname']
            c_lastname=request.POST['_lastname']
            c_gender=request.POST['_gender']
            c_dateofbirth=request.POST['_dateofbirth']
            c_address=request.POST['_address']
            c_country=request.POST['_country']
            c_mobilenumber=request.POST['_mobilenumber']
            c_email=request.POST['_email']
            c_password=request.POST['_password']
            customer_exists=Customer.objects.filter(email=c_email).exists()

            if not customer_exists:
                otp=randint(1000,999)
                send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [email],

                )
                customer_data=Customer(first_name=c_firstname,last_name=c_lastname,gender=c_gender,dateofbirth=c_dateofbirth,address=c_address,country=c_country,mobilenumber=c_mobilenumber,email=c_email,password=c_password,otp=str(otp),status='otp verified')
                customer_data.save()
                msg='customer registerd successfully' 

                
    return render(request,"customer/signup.html",{'message':msg})




def getcustomerverifyotp(request):
    return render(request,"customer/verifyotp.html")


def getcustomerlogin(request):
    return render(request,"customer/login.html")

def getcustomerprofile(request):
    return render(request,"customer/profile.html")

def getcustomers(request):
    return render(request,"customer/search.html")

def getmaster2(request):
    return render(request,"customer/master2.html")

def getviewproduct(request):
    return render(request,"customer/viewproduct.html")

def getloginhomepage(request):
    return render(request,"customer/loginhomepage.html")

def getbag(request):
    return render(request,"customer/bag.html")

def getbuynow(request):
    return render(request,"customer/buynow.html")