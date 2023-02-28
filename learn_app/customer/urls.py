from django. urls import path
from . import views
app_name='customer'

urlpatterns = [
    path('master1/',views.registercustomer,name="master1"),
    path('homepage1/',views.registercustomer,name="homepage1"),
    path('signup/',views.registercustomer,name="signup"),
    path('login/',views.registercustomer,name="login"),
    path('account1/',views.registercustomer,name="account1"),
    path('search/',views.registercustomer,name="search"),
    path('master2/',views.registercustomer,name="master2"),
]