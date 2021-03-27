from django.contrib import admin
from .models import PlayerInfo, PlayerSeasonWiseStats

# Register your models here.
admin.site.register(PlayerInfo)
admin.site.register(PlayerSeasonWiseStats)
