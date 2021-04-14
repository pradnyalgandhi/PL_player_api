from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import ConsumerForm

from rest_framework_simplejwt.tokens import RefreshToken

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
            return redirect('login')
    else:
        form = ConsumerForm()
    return render(request,"consumer/login_form.html",{'form':form})


  