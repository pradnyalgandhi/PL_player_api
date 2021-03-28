from django.db import models

class PlayerInfo(models.Model):

    POSITION = [('FWD','Forward'),
               ('Mid','Midfielder'),
               ('Def','Defender'),
               ('Gk','Goalkeeper')]

    name = models.CharField(max_length= 50, blank=False)
    jersey_no = models.IntegerField(blank=True, null=True)
    current_club = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=10,choices=POSITION, default="Not Assigned") 
    apps = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class PlayerSeasonWiseStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete= models.CASCADE)
    season = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    apps = models.CharField(max_length=50)
    goals = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.club}: {self.season}"

class AttackingStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    goals = models.IntegerField(blank=True, null=True, default=0)
    headers = models.IntegerField(blank=True, null=True, default=0)
    right_foot_goals = models.IntegerField(blank=True, null=True, default=0)
    left_foot_goals = models.IntegerField(blank=True, null=True, default=0)
    penalties = models.IntegerField(blank=True, null=True, default=0)
    freekicks = models.IntegerField(blank=True, null=True, default=0)
    shots = models.IntegerField(blank=True, null=True, default=0)
    shots_on_target = models.IntegerField(blank=True, null=True, default=0)
    accuracy = models.IntegerField(blank=True, null=True, default=0)
    hit_woodwork = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.name} - Goals: {self.goals}"

class DefensiveStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    clean_sheets = models.IntegerField(blank=True, null=True, default=0)
    goals_conceded = models.IntegerField(blank=True, null=True, default=0)
    tackles = models.IntegerField(blank=True, null=True, default=0)
    tacles_success_rate = models.IntegerField(blank=True, null=True, default=0)
    blocked_shots = models.IntegerField(blank=True, null=True, default=0)
    interceptions = models.IntegerField(blank=True, null=True, default=0)
    recoveries = models.IntegerField(blank=True, null=True, default=0)
    duels_won = models.IntegerField(blank=True, null=True, default=0)
    dues_lost = models.IntegerField(blank=True, null=True, default=0)
    successful_50_50 = models.IntegerField(blank=True, null=True, default=0)
    aerial_battles_won = models.IntegerField(blank=True, null=True, default=0)
    aerial_battles_lost = models.IntegerField(blank=True, null=True, default=0)
    own_goals = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.name} - Clean Sheets: {self.clean_sheets}"

class DisciplinaryStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    yellow_cards = models.IntegerField(blank=True, null=True, default=0)
    red_cards = models.IntegerField(blank=True, null=True, default=0)
    fouls = models.IntegerField(blank=True, null=True, default=0)
    offsides = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return f"{self.name}"


class TeamPlayStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete= models.CASCADE)
    assists = models.IntegerField(blank=True, null=True, default=0)
    total_passes = models.IntegerField(blank=True, null=True, default=0)
    passes_per_match = models.IntegerField(blank=True, null=True, default=0)
    chances_created = models.IntegerField(blank=True, null=True, default=0)
    crosses = models.IntegerField(blank=True, null=True, default=0)
    cross_accuracy = models.IntegerField(blank=True, null=True, default=0)
    through_balls = models.IntegerField(blank=True, null=True, default=0)
    long_balls = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return "{self.name} - Assists : {self.assists}"


