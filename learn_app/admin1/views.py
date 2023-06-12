from django.shortcuts import render
from reseller.models import Reseller
# Create your views here.


def getadmin1(request):
    return render(request,"admin1/homepage.html")

def getmaster3(request):
    return render(request,"admin1/master3.html")

def getmanageresellers(request):
    reseller_data=Reseller.objects.filter(status='inactive')
    if request.method=="POST":
        seller_id=request.POST['reseller_id']
        reseller=Reseller.objects.get(id=seller_id)
        if 'approve' in request.POST:
            reseller.status='active'
        if 'reject' in request.POST:
            reseller.status='reject'
        reseller.save()
    return render(request,"admin1/manageresellers.html",{'resellers':reseller_data})

def getactiveresellers(request):
    reseller_data=Reseller.objects.filter(status='active')
    


    return render(request,"admin1/activeresellers.html",{'resellers':reseller_data})
 
def getrejectedresellers(request):
    reseller_data=Reseller.objects.filter(status='reject')
    return render(request,"admin1/rejectedresellers.html",{'resellers':reseller_data})

def getsum(request):
    result=""
    if request.method=="POST":
        num1=int(request.POST['frstnum'])
        num2=int(request.POST['scndnum'])
        result=num1+num2
    return render(request,"admin1/sum.html",{'res':result})
 
 