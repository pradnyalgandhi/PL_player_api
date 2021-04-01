from django.shortcuts import render
from .update_db import update_model
from .models import PlayerInfo

from django.views.generic import TemplateView, DetailView, ListView
import requests

def home(request):
   return render(request, 'api/home.html')

class Player(TemplateView):
   model = PlayerInfo
   template_name = "api/check.html"
   context_object_name = 'player'

   def get_context_data(self,*args,**kwargs):
      context = super().get_context_data(**kwargs)
      context['player'] = PlayerInfo.objects.all()
      return context


def update_models(request):   
   if request.method == "POST":
      status = update_model()
      if status == "OK":
         return render(request, "api/update_db.html")
   return render(request, "api/update_db.html")

class Documentation(TemplateView):
   template_name = "api/documentation.html"



