from django. urls import path
from . import views
app_name = 'reseller'

urlpatterns = [
    path('homepage2/',views.gethomepage2,name="homepage2"),
    path('login1/',views.getlogin1,name="login1"),
    path('signup1/',views.getsignup1,name="signup1"),
    path('addproduct/',views.getaddproduct,name="addproduct"),
    path('master/',views.getmaster,name="master"),
    path('edit/',views.getedit,name="edit"),   
    path('myproducts/',views.getmyproducts,name="myproducts"), 
    path('account/',views.getaccount,name="account"),   
    path('vieworders/',views.getvieworders,name="vieworders"),
    # path('updateproduct/<int:s_id>',views.update_products,name="updateproducts"),   
    # path('deleteproduct/<int:s_id>',views.delete_products,name="deleteproducts"),  
    path('viewproducts_demo',views.getviewproducts_demo,name="viewproducts_demo"),
    path('deleteproducts/<int:p_id>',views.deleteproducts,name="delete_product"),    
    path('updation_demo/<int:p_id>',views.getupdationdemo,name="_updationdemo"),

   ]
