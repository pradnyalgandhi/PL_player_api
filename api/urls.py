from django.urls import path
from api.views import ( PlayerInfoList,
                        PlayerSeasonWiseStatsList,
                        PlayerAttackingStatsList,
                        PlayerDefensiveStatsList,
                        PlayerDisciplinaryStatsList,
                        PlayerTeamPlayStatsList,
                        PlayerGoalKeepingStatsList)

urlpatterns = [
    path('player_info/', PlayerInfoList.as_view(), name="player-info"),
    path('player_attacking_stats/', PlayerAttackingStatsList.as_view(), name="plasyer-attacking_stat"),
    path('player_defensive_stats/', PlayerDefensiveStatsList.as_view(), name="plasyer-defensive-stat"),
    path('player_disciplinary_stats/', PlayerDisciplinaryStatsList.as_view() , name="player-disciplinary-stat"),
    path('player_teamplay_stats/', PlayerTeamPlayStatsList.as_view(), name="player-teamplay-stat"),
    path('player_goalkeeping_stats/', PlayerGoalKeepingStatsList, name="player-goalkeeping-stat"),
]