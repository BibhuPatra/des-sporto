from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Players(models.Model):

    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email

class Institute(models.Model):

    institute_id = models.AutoField(primary_key=True)
    # auth_id = models.ForeignKey(User,on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    no_coaches = models.CharField(max_length=100)
    no_players = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    age_group = models.CharField(max_length=100)

    def __str__(self):
        return self.institute_name
    
    