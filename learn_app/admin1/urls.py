from django. urls import path
from . import views
app_name= 'admin1'

urlpatterns = [
    path('homepage/',views.getadmin1,name="homepage"),
    path('master3/',views.getmaster3,name="master3"),
    path('manageresellers/',views.getmanageresellers,name="manageresellers"),
    path('activeresellers/',views.getactiveresellers,name="activeresellers"),
    path('rejectedresellers/',views.getrejectedresellers,name="rejectedresellers"),
    path('sum/',views.getsum,name="sum"),
]