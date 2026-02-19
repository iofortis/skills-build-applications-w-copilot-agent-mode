from django.db import models
from django.contrib.auth.models import User

# Create your models here.


from teams.models import Team

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    bio = models.TextField(blank=True)
    age = models.IntegerField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    fitness_level = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username
