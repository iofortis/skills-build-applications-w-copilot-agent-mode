from django.db import models


from users.models import Profile

class Workout(models.Model):
	user = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.name} - {self.user.user.username}"
