from django. urls import path
from . import views
app_name= 'admin1'

urlpatterns = [
    path('homepage/',views.getadmin1,name="homepage"),
    path('master3/',views.getmaster3,name="master3"),
    path('addresellers/',views.getaddresellers,name="addresellers"),
    path('managereseller/',views.getmanagereseller,name="managereseller"),
    path('delete/',views.getdelete,name="delete"),
]