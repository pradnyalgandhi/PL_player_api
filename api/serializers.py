from rest_framework import serializers
from .models import (PlayerInfo,
                     PlayerSeasonWiseStats,
                     AttackingStats,
                     DefensiveStats,
                     DisciplinaryStats,
                     TeamPlayStats,
                     GoalkeepingStats)


class PlayerSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerInfo
        fields = "__all__"

class PlayerSeasonSerializers(serializers.ModelSerializer):
    class Meta:
        model = PlayerSeasonWiseStats
        fields = "__all__"

class PlayerAttackingStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = AttackingStats
        fields = "__all__"

class PlayerDefensiveStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DefensiveStats
        fields = "__all__"

class PlayerDisciplinaryStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DisciplinaryStats
        fields = "__all__"

class PlayerTeamPlayStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeamPlayStats
        fields = "__all__"

class PlayerGoalkeepingStatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoalkeepingStats
        fields = "__all__"