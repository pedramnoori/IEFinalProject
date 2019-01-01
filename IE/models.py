from django.contrib.auth.models import User
from django.db import models
import string, random

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=50,default="TEST")
    score = models.IntegerField(default=0)
    buildDate = models.DateTimeField(auto_now=True)
    maxScore = models.IntegerField(default=0)
    holdDices = models.CharField(max_length=10)
    diceNumber = models.IntegerField(default=1)
    maxRoll = models.IntegerField(default=4)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='create')
    playCount = models.IntegerField(default=0)
    averageScore = models.FloatField(default=0)


class GameData:
    def __init__(self, dice_count, max_score, hold):
        self.id = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=32))
        self.dices = []
        self.dice_count = dice_count
        self.turn = True
        self.max_score = max_score
        self.player1_current = 0
        self.player1_total = 0
        self.player2_current = 0
        self.player2_total = 0
        self.winner = None
        self.hold = hold