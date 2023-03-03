from django. urls import path
from . import views
app_name='customer'

urlpatterns = [
    path('master1/',views.getmaster,name="master1"),
    path('homepage1/',views.getcustomerhomepage,name="homepage1"),
    path('signup/',views.getcustomersign,name="signup"),
    path('login/',views.getcustomerlogin,name="login"),
    path('profile/',views.getcustomerprofile,name="profile"),
    path('search/',views.getcustomers,name="search"),
    path('master2/',views.getmaster2,name="master2"),
    path('viewproduct/',views.getviewproduct,name="viewproduct"),
    path('loginhomepage/',views.getloginhomepage,name="loginhomepage"),
]
