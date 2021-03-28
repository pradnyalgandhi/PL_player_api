from django.shortcuts import render
import requests, json
from .scraper import PlayerStats
from .models import PlayerInfo, PlayerSeasonWiseStats, AttackingStats, DefensiveStats, DisciplinaryStats, TeamPlayStats


def scrapped_data(request):

   url = "https://www.premierleague.com/players/"

   data = PlayerStats(url)
   data_library = data.get_data()
   PlayerInfo.objects.all().delete()  
   for item in data_library:       
      
      player = PlayerInfo(
                          name=item['Name'],
                          jersey_no=item["Jersey No"],
                          current_club= item["Current Club"],
                          nationality= item["Nationality"],
                          position= item["Position"],
                          apps= item["Appearances"],
                          goals = item["Goals"],
                          wins = item["Total Wins"],
                          losses = item["Total Losses"]
                          )
      player.save()

      for stat in item['Career']:
         player_season = PlayerSeasonWiseStats(
                          name= player,
                          season = stat['Season'],
                          club = stat['Club'],
                          apps = stat['Apps'],
                          goals = stat['Goals']
         )
         player_season.save()

      # Loop for Atk,def, dis and teamplay stats 
   # print(name,current_club,nationality, position)  
   


   return render(request, 'api/home.html')