from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings
from reseller.models import Reseller
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
                otp=randint(1000,9999)
                send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [c_email],

                )
                customer_data=Customer(first_name=c_firstname,last_name=c_lastname,gender=c_gender,dateofbirth=c_dateofbirth,address=c_address,country=c_country,mobilenumber=c_mobilenumber,email=c_email,password=c_password,otp=str(otp),status='otp verified')
                customer_data.save()
                # msg='customer registerd successfully'
                return redirect('customer:verifyotp') 
        
        if user_type=='reseller':
            r_company_name=request.POST['_company_name']
            r_company_id=request.POST['reg_id']
            r_account_num=request.POST['_account_no']
            r_ifsc_code=request.POST['_ifsc_code']
            r_bank_name=request.POST['_branch_name']
            r_address=request.POST['_address']
            r_country=request.POST['_country']
            r_mobilenumber=request.POST['_mobilenumber']
            r_email=request.POST['_email']
            r_password=request.POST['_password']
            r_otp=randint(1000,9999)
            reseller_exists=Reseller.objects.filter(email=r_email).exists()
            if not reseller_exists:
                reseller=Reseller(company_name=r_company_name,reg_id=r_company_id,account_number=r_account_num,ifsc_code=r_ifsc_code,address=r_address,country=r_country,mobile=r_mobilenumber,email=r_email,password=r_password)
                reseller.save()
                subject='your login id is '+str(r_otp)
                send_mail(
                    'login credentials',
                    subject,
                    settings.EMAIL_HOST_USER,
                    [r_email],

                )
                msg='registration successful'
            else:
                msg='email exists'
            return render(request,'customer/signup.html',{'message':msg})
    return render(request,"customer/signup.html")




def getcustomerverifyotp(request):
    # if request.method=='POST':
    #     otp=request.POST['o_tp']s

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
