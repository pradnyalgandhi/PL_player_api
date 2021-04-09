from django.db import models

class PlayerInfo(models.Model):

    POSITION = [('FWD','Forward'),
               ('Mid','Midfielder'),
               ('Def','Defender'),
               ('Gk','Goalkeeper')]

    name = models.CharField(max_length= 50, blank=False, primary_key=True)
    jersey_no = models.CharField(max_length=20, blank=True)
    current_club = models.CharField(max_length=50, null=True)
    nationality = models.CharField(max_length=50, null=True)
    position = models.CharField(max_length=10,choices=POSITION, default="Not Assigned") 
    apps = models.CharField(max_length=50, null=True)
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
    goals = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    headers = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    right_foot_goals = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    left_foot_goals = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    penalties = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    freekicks = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    shots = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    shots_on_target = models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    accuracy = models.CharField(max_length=50, null=True)
    hit_woodwork = models.CharField(max_length=50,blank=True, null=True, default="Not Available")

    def __str__(self):
        return f"{self.name} - Goals: {self.goals}"

class DefensiveStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    clean_sheets = models.CharField(max_length = 50 ,blank=True, null=True, default="Not Available")
    goals_conceded = models.CharField(max_length = 50, blank=True, null=True, default="Not Available")
    tackles = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    tacles_success_rate = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    clearances = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    blocked_shots = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    interceptions = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    recoveries = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    duels_won = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    dues_lost = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    successful_50_50 = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    aerial_battles_won = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    aerial_battles_lost = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    own_goals = models.CharField(max_length=50, blank=True, null=True, default="Not Available")

    def __str__(self):
        return f"{self.name} - Clean Sheets: {self.clean_sheets}"

class DisciplinaryStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    yellow_cards = models.CharField(max_length=50, blank=True, null=True, default="Not Available")
    red_cards = models.IntegerField(blank=True, null=True, default="0")
    fouls = models.CharField(max_length = 50,blank=True, null=True, default="Not Available")
    offsides = models.CharField(max_length= 20, blank=True, null=True, default="Not Available")

    def __str__(self):
        return f"{self.name}"


class TeamPlayStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete= models.CASCADE)
    assists = models.CharField(max_length = 50,blank=True, null=True, default="Not Available")
    total_passes = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    passes_per_match = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    chances_created = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    crosses = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    cross_accuracy = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    through_balls = models.CharField(max_length=20, blank=True, null=True, default="Not Available")
    long_balls = models.CharField(max_length=20, blank=True, null=True, default="Not Available")

    def __str__(self):
        return f"{self.name} - Assists : {self.assists}"


class GoalkeepingStats(models.Model):
    name = models.ForeignKey(PlayerInfo, on_delete=models.CASCADE)
    clean_sheets =  models.IntegerField(blank=True, null=True, default="Not Available")
    saves =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    penalties_saved =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    punches =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    high_claims =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    catches =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    sweeper_clearance =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    throw_outs =  models.CharField(max_length=50,blank=True, null=True, default="Not Available")
    goal_kicks =  models.CharField(max_length= 100, blank=True, null=True, default="Not Available")

    def __str__(self):
        return f"{self.name} - Clean Sheets : {self.clean_sheets}"


class PlayerData(models.Model):
    name = models.CharField(max_length= 50, null=False)
    jersey_no = models.CharField(max_length=20, blank=True)
    current_club = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=20, blank=True)
    position = models.CharField(max_length=20, blank=True)
    apps = models.IntegerField()
    wins = models.IntegerField()
    losses = models.IntegerField()
    goals = models.CharField(max_length=20, blank=True)
    headers = models.CharField(max_length=20, blank=True)
    right_foot_goals = models.CharField(max_length=20, blank=True)
    left_foot_goals = models.CharField(max_length=20, blank=True)
    penalties = models.CharField(max_length=20, blank=True)
    freekicks = models.CharField(max_length=20, blank=True)
    shots = models.CharField(max_length=20, blank=True)
    shots_on_target = models.CharField(max_length=20, blank=True)
    accuracy = models.CharField(max_length=20, blank=True)
    hit_woodwork = models.CharField(max_length=20, blank=True)
    clean_sheets = models.CharField(max_length=20, blank=True)
    goals_conceded = models.CharField(max_length=20, blank=True)
    tackles = models.CharField(max_length=20, blank=True)
    tackles_success_rate = models.CharField(max_length=20, blank=True)
    clearances = models.CharField(max_length=20, blank=True)
    blocked_shots = models.CharField(max_length=20, blank=True)
    interceptions = models.CharField(max_length=20, blank=True)
    recpveries = models.CharField(max_length=20, blank=True)
    duels_won = models.CharField(max_length=20, blank=True)
    dues_lost = models.CharField(max_length=20, blank=True)
    successfull_50_50 = models.CharField(max_length=20, blank=True)
    aerial_battles_won = models.CharField(max_length=20, blank=True)
    aerial_battles_lost = models.CharField(max_length=20, blank=True)
    own_goals = models.CharField(max_length=20, blank=True)
    yellow_cards = models.IntegerField()
    red_cards = models.IntegerField()
    fouls = models.IntegerField()
    offsides = models.CharField(max_length=20, blank=True)
    assists = models.IntegerField()
    total_passes = models.CharField(max_length=20, blank=True)
    passes_per_match = models.CharField(max_length=20, blank=True)
    chances_created = models.CharField(max_length=20, blank=True)
    crosses = models.CharField(max_length=20, blank=True)
    cross_accuracy = models.CharField(max_length=20, blank=True)
    through_balls = models.CharField(max_length=20, blank=True)
    long_balls = models.CharField(max_length=20, blank=True)

    





