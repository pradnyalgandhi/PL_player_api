from django.urls import path
from .views import login_form

urlpatterns = [
    path('login/', login_form, name= "consumer-login" ),
]