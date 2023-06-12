from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.mail import send_mail 
from django.conf import settings
from reseller.models import Add_product
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
                customer_data=Customer(first_name=c_firstname,last_name=c_lastname,gender=c_gender,dateofbirth=c_dateofbirth,address=c_address,country=c_country,mobilenumber=c_mobilenumber,email=c_email,password=c_password,otp=str(otp),status='otpverify')
                customer_data.save()
                customer=Customer.objects.get(email=c_email)
                request.session['customer_id']=customer.id

                # msg='customer registerd successfully'
                return redirect('customer:verifyotp') 
    #           return render(request,'customer/signup.html',{'message':msg})
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
            r_loginid=randint(1000,9999)
            reseller_exists=Reseller.objects.filter(email=r_email).exists()
            if not reseller_exists:
                reseller=Reseller(company_name=r_company_name,reg_id=r_company_id,account_number=r_account_num,ifsc_code=r_ifsc_code,address=r_address,country=r_country,mobile=r_mobilenumber,email=r_email,user_id=r_loginid,password=r_password)
                reseller.save()
                subject='your login id is '+str(r_loginid)
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
    if request.method=='POST':
        otp=request.POST['o_tp']
        c_id=request.session['customer_id']
        data=Customer.objects.get(id=c_id)
        if otp==data.otp:
            Customer.objects.filter(id=c_id).update(status='active')
            return redirect('customer:loginhomepage')
        else:
            return render(request,"customer/verifyotp.html",{'message':'invalid otp'})

    return render(request,"customer/verifyotp.html")

 
def getcustomerlogin(request):
    if request.method=="POST":
        _username=request.POST['username']
        _password=request.POST['password']
        if '@' in _username:
            customer_exist=Customer.objects.filter(email=_username,password=_password).exists()
            if customer_exist:
                customer=Customer.objects.get(email=_username,password=_password)
                request.session['customer_id']=customer.id
                if customer.status=='otpverify':
                    otp=randint(1000,9999)
                    send_mail(
                    'please verify your otp',
                    str(otp),
                    settings.EMAIL_HOST_USER,
                    [customer.email],
                
                    )

                    customer.otp=otp
                    customer.save()
                    return redirect('customer:verifyotp')
                return redirect('customer:loginhomepage')
            else:
                return render(request,"customer/login.html",{'message':'invalid user details'})

        elif _username.isdigit():
            seller_exist=Reseller.objects.filter(user_id=_username,password=_password).exists()
            
            if seller_exist:
                seller_data=Reseller.objects.get(user_id=_username,password=_password)
                if seller_data.status=='active':
                    request.session['seller_id']=seller_data.id
                    return redirect('reseller:homepage2')
                else:
            
            
                    return render(request,"customer/login.html",{'message':'account not approved'})
            else:
                return render(request,"customer/login.html",{'message':'invalid user name or password'})
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
    products=Add_product.objects.all()
    return render(request,"customer/loginhomepage.html",{'product_data':products})

def getbag(request):
    return render(request,"customer/bag.html")

def getbuynow(request):
    return render(request,"customer/buynow.html")
