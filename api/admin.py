from django.contrib import admin
from .models import (PlayerInfo, 
                    PlayerSeasonWiseStats, 
                    AttackingStats, 
                    GoalkeepingStats, 
                    DisciplinaryStats, 
                    TeamPlayStats,
                    DefensiveStats)

# Register your models here.
admin.site.register(PlayerInfo)
admin.site.register(PlayerSeasonWiseStats)
admin.site.register(AttackingStats)
admin.site.register(GoalkeepingStats)
admin.site.register(TeamPlayStats)
admin.site.register(DisciplinaryStats)
admin.site.register(DefensiveStats)
