from django.db import models


# Model for storing teams
class Teams(models.Model):
    teamName = models.CharField(max_length=50, unique=True)
    manager = models.CharField(max_length=50)
    coach = models.CharField(max_length=50)
    player1 = models.CharField(max_length=20)
    player2 = models.CharField(max_length=20)
    player3 = models.CharField(max_length=20)
    player4 = models.CharField(max_length=20)
    player5 = models.CharField(max_length=20)
    player6 = models.CharField(max_length=20)
    player7 = models.CharField(max_length=20)
    player8 = models.CharField(max_length=20)
    player9 = models.CharField(max_length=20)
    player10 = models.CharField(max_length=20)
    player11 = models.CharField(max_length=20)
    goals = models.IntegerField(null=True)
    wins = models.IntegerField(null=True)
    fails = models.IntegerField(null=True)
    score = models.FloatField(null=True)

    def __str__(self):
        return self.teamName


# Model for setting venues
class Venues(models.Model):
    venue = models.CharField(max_length=50)

    def __str__(self):
        return self.venue


# Model for generating fixture
class Matches(models.Model):
    team1 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team1')
    team2 = models.ForeignKey(Teams, on_delete=models.PROTECT, related_name='team2')
    date = models.DateField()
    venue = models.ForeignKey(Venues, on_delete=models.PROTECT)
    team1_score = models.IntegerField(null=True)
    team2_score = models.IntegerField(null=True)
    match_over = models.BooleanField(default=False)

    def __str__(self):
        return self.team1, self.team2

