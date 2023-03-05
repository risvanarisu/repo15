from django.shortcuts import render

# Create your views here.


def getmaster(request):
    return render(request,"customer/master1.html")
    
def getcustomerhomepage(request):
    return render(request,"customer/homepage1.html")

def getcustomersign(request):
    return render(request,"customer/signup.html")

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