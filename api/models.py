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

# class AttackingStats(models.Model):
