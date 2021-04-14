from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .update_db import update_model
from .models import PlayerInfo, PlayerSeasonWiseStats, AttackingStats, DefensiveStats, TeamPlayStats, GoalkeepingStats, DisciplinaryStats, PlayerData
from .serializers import (PlayerSerializers, 
                          PlayerSeasonSerializers,
                          PlayerAttackingStatsSerializers,
                          PlayerDefensiveStatsSerializers,
                          PlayerDisciplinaryStatsSerializers,
                          PlayerTeamPlayStatsSerializers,
                          PlayerGoalkeepingStatsSerializers,
                          )

from django.views.generic import TemplateView

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser


def home(request):
   return render(request, 'api/home.html')

@login_required
def update_models(request):
   if request.method == "POST":
      status = update_model()
      if status == "OK":
         return render(request, "api/update_db.html")
   return render(request, "api/update_db.html")

class Documentation(TemplateView):
   template_name = "api/documentation.html"

#Serializers
class PlayerInfoList(generics.ListAPIView):
   queryset = PlayerInfo.objects.all()
   serializer_class = PlayerSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerSeasonWiseStatsList(generics.ListAPIView):
   queryset = PlayerSeasonWiseStats.objects.all()
   serializer_class = PlayerSeasonSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerAttackingStatsList(generics.ListAPIView):
   queryset = AttackingStats.objects.all()
   serializer_class = PlayerAttackingStatsSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerDefensiveStatsList(generics.ListAPIView):
   queryset = DefensiveStats.objects.all()
   serializer_class = PlayerDefensiveStatsSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerDisciplinaryStatsList(generics.ListAPIView):
   queryset = DisciplinaryStats.objects.all()
   serializer_class = PlayerDisciplinaryStatsSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerTeamPlayStatsList(generics.ListAPIView):
   queryset = TeamPlayStats.objects.all()
   serializer_class = PlayerTeamPlayStatsSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]

class PlayerGoalKeepingStatsList(generics.ListAPIView):
   queryset = GoalkeepingStats.objects.all()
   serializer_class = PlayerGoalkeepingStatsSerializers
   permission_classes = [IsAuthenticatedOrReadOnly]


