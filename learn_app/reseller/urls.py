from django. urls import path
from . import views

urlpatterns = [
    path('homepage2/',views.registerreseller,name="homepage2"),
]