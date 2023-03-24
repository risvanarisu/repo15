from django.shortcuts import render

# Create your views here.

def gethomepage2(request):
    return render(request,"reseller/homepage2.html")

def getlogin1 (request):
    return render(request,"reseller/login1.html")
 
def getsignup1(request):
    return render(request,"reseller/signup1.html")
 
def getaddproduct(request):
    return render(request,"reseller/addproduct.html")

def getmaster(request):
    return render(request,"reseller/master.html")

def getedit(request):
    return render(request,"reseller/edit.html")

def getmyproducts(request):
    return render(request,"reseller/myproducts.html")

def getaccount(request):
    return render(request,"reseller/account.html")
 
def getvieworders(request):
    return render(request,"reseller/vieworders.html")
 


 