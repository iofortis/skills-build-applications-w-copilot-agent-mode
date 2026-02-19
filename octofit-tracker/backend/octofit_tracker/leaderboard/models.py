from django.db import models


from users.models import Profile

class Leaderboard(models.Model):
	user = models.OneToOneField(Profile, on_delete=models.CASCADE)
	points = models.IntegerField(default=0)

	def __str__(self):
		return f"{self.user.user.username} - {self.points} pts"
