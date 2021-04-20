from django.urls import path
from .views import login_form, profile

urlpatterns = [
    path('register/', login_form, name= "consumer-register" ),
    path('profile/',profile, name="profile")
]