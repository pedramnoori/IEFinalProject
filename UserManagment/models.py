from django.db import models
from django.contrib.auth.models import User as u

# Create your models here.

class User(u):
    # username = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    sex = models.CharField(max_length=10)
    birthDate = models.DateField()
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    photo = models.FileField()
    # email = models.EmailField()
    numberOfAllGames = models.IntegerField( null=True)
    averageOfGameScore = models.FloatField(max_length=4, null=True)
    averageOfUserScore = models.FloatField(max_length=100, null=True)
    isAdmin = models.BooleanField(null=True)
