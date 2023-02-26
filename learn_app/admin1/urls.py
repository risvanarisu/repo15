from django. urls import path
from . import views

urlpatterns = [
    path('homepage/',views.registeradmin1,name="homepage"),
]