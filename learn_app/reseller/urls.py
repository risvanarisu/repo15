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
]  
