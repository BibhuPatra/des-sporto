from django.db import models

# Create your models here.

class Players(models.Model):

    player_id = models.AutoField(primary_key=True)
    player_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
    