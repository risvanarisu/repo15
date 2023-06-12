from django.shortcuts import render,redirect
from .models import *
from django.conf import settings
# Create your views here.

def gethomepage2(request):
    return render(request,"reseller/homepage2.html")

def getlogin1 (request):
    return render(request,"reseller/login1.html")
 
def getsignup1(request):
    return render(request,"reseller/signup1.html")
 
def getaddproduct(request):
    if request.method=='POST':
        p_title=request.POST['_title']
        p_regid=request.POST['_Registered_product_id']
        p_discription=request.POST['_discription']
        p_picture=request.FILES['_picture']
        p_price=request.POST['_price']
        p_quantity=request.POST['_quantity']
        p_weight=request.POST['_weight']
        p_weightunit=request.POST['_weight_unit']
        p_catagory=request.POST['_catagory']
        p_subcatagory=request.POST['_subcatagory']
        p_brand=request.POST['_brand']
        #p_status=request.POST['_status']
        p_resellerid=Reseller.objects.get(id=request.session['seller_id'])
        product_exists=Add_product.objects.filter(pro_id=p_regid)
        if not product_exists:

            product=Add_product(title=p_title,pro_id=p_regid,discription=p_discription,pro_picture=p_picture,price=p_price,quantity=p_quantity,weight=p_weight,weight_unit=p_weightunit,catagory=p_catagory,sub_catagory=p_subcatagory,brand=p_brand,reseller=p_resellerid)
            product.save()
            return render(request,"reseller/addproduct.html",{'message':'product added successfully'})
        else:
            return render(request,"reseller/addproduct.html",{'message':'product already exists'})
        
    return render(request,"reseller/addproduct.html")

def getmaster(request):
    return render(request,"reseller/master.html")

def getedit(request):
    # title1=request.POST['ti_tle']
    # regid1=request.POST['pr_id']
    # discription1=request.POST['pr_ad']
    # picture1=request.FILES['pr_im']
    # price1=request.POST['pr_price']
    # quantity1=request.POST['pr_quant']
    # weight1=request.POST['pr_weight']
    # weightunit1=request.POST['pr_unit']
    # catagory1=request.POST['pr_cat']
    # subcatagory1=request.POST['pr_subcat']
    # brand1=request.POST['pr_brand']
    
    # prod=Add_product.objects.get(title=title1,pro_id=regid1,discription=discription1,pro_picture=picture1,price=price1,quantity=quantity1,weight=weight1,weight_unit=weightunit1,catagory=catagory1,sub_catagory=subcatagory1,brand=brand1)

    return render(request,"reseller/edit.html")

def getmyproducts(request):
    products=Add_product.objects.all()
   
    return render(request,"reseller/myproducts.html",{'product_data':products})

def getaccount(request):
    return render(request,"reseller/account.html")
 
def getvieworders(request):
    return render(request,"reseller/vieworders.html")

# def update_products(request,s_id):
    
#     title1=request.POST['ti_tle']
#     regid1=request.POST['pr_id']
#     discription1=request.POST['pr_ad']
#     picture1=request.FILES['pr_im']
#     price1=request.POST['pr_price']
#     quantity1=request.POST['pr_quant']
#     weight1=request.POST['pr_weight']
#     weightunit1=request.POST['pr_unit']
#     catagory1=request.POST['pr_cat']
#     subcatagory1=request.POST['pr_subcat']
#     brand1=request.POST['pr_brand']
    
#     Add_product.objects.filter(id=s_id).update(title=title1,pro_id=regid1,discription=discription1,pro_picture=picture1,price=price1,quantity=quantity1,weight=weight1,weight_unit=weightunit1,catagory=catagory1,sub_catagory=subcatagory1,brand=brand1)
    
    
#     product=Add_product.objects.get(id=s_id)
    
    
     
#     return redirect('reseller:edit')

# def delete_products(request,s_id):
#     product=Add_product.objects.get(id=s_id)
#     product.delete()
#     return redirect('reseller:myproducts')   
 
# demo updation deletion
def getviewproducts_demo(request):
    product=Add_product.objects.all()

    return render(request,"reseller/viewproducts_demo.html",{'product_data':product})

def deleteproducts(request,p_id):
    Add_product.objects.get(id=p_id).delete()
    return redirect('reseller:viewproducts_demo')

# end demo updation deletion 


def getupdationdemo(request,p_id):
    if request.method=='POST':
        title_=request.POST['_title']
        prid_=request.POST['_Registered_product_id']
        discription_=request.POST['_discription']
        price_=request.POST['_price']
        quantity_=request.POST['_quantity']
        Add_product.objects.filter(id=p_id).update(title=title_,pro_id=prid_,discription=discription_,price=price_,quantity=quantity_)
        return redirect('reseller:viewproducts_demo')


    product=Add_product.objects.get(id=p_id)
   

    return render(request,"reseller/updationdemo.html",{'product_data':product})