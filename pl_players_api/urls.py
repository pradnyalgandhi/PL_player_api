"""pl_players_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from api.views import (home, 
                        update_models , 
                        Documentation, 
                        Player)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('login', auth_views.LoginView.as_view(template_name = 'api/login.html')),
    path('update_db/',update_models, name="update-database"),
    path('check/', Player.as_view(), name= "check"),
    path('docs/', Documentation.as_view(), name= "docs"),
    path('accounts/login/', home),
]
