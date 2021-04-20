from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ConsumerForm, ConsumerUpdateForm

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

# Create your views here.
def login_form(request):
    if request.method == "POST":
        form = ConsumerForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = ConsumerForm()
    return render(request,"consumer/register.html",{'form':form})

@login_required
def profile(request):
    if request.method == "POST":
        update_form = ConsumerUpdateForm(request.POST, instance=request.user)        
        if update_form.is_valid():
            update_form.save()            
            return redirect('profile')
    else:
        update_form = ConsumerUpdateForm(instance=request.user)
    return render(request,"consumer/profile.html",{'update_form': update_form})

