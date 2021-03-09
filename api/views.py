from django.shortcuts import render
import requests
from .scraper import PlayerStats
from bs4 import BeautifulSoup

# Create your views here.
def home(requests):   
    return render(requests, 'api/home.html')
