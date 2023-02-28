from django. urls import path
from . import views
app_name='reseller'

urlpatterns = [
    path('homepage2/',views.registerreseller,name="homepage2"),
    path('login1/',views.registerreseller,name="login1"),
    path('signup1/',views.registerreseller,name="signup1"),
    path('addproduct/',views.registerreseller,name="addproduct"),
    path('master/',views.registerreseller,name="master"),
    path('edit/',views.registerreseller,name="edit"),
    path('order/',views.registerreseller,name="order"),   
    path('myproducts/',views.registerreseller,name="myproducts"), 
    path('account/',views.registerreseller,name="account"),   
]  
