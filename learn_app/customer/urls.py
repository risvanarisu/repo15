from django. urls import path
from . import views

urlpatterns = [
    path('homepage1/',views.registercustomer,name="homepage1"),
]