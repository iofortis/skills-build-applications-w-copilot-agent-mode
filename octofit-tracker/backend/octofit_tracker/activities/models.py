from django.db import models


from users.models import Profile

class Activity(models.Model):
	ACTIVITY_TYPES = [
		('run', 'Run'),
		('cycle', 'Cycle'),
		('swim', 'Swim'),
	]
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	type = models.CharField(max_length=20, choices=ACTIVITY_TYPES)
	duration = models.PositiveIntegerField(help_text='Duration in minutes')
	distance = models.FloatField(help_text='Distance in kilometers')
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.user.user.username} - {self.type}"
