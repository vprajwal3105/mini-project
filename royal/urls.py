from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path("register/", views.register, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("car_model",views.car_model,name="car_model")
    
   
]