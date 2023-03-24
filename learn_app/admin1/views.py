from django.shortcuts import render

# Create your views here.


def getadmin1(request):
    return render(request,"admin1/homepage.html")

def getmaster3(request):
    return render(request,"admin1/master3.html")

def getaddresellers(request):
    return render(request,"admin1/addresellers.html")

def getmanagereseller(request):
    return render(request,"admin1/managereseller.html")
 
def getdelete(request):
    return render(request,"admin1/delete.html")
 
 