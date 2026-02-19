from django.test import TestCase


from .models import Workout
from users.models import Profile
from teams.models import Team
from django.contrib.auth.models import User
from django.test import TestCase

class WorkoutModelTest(TestCase):
	def test_create_workout(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team')
		profile = Profile.objects.create(user=user, team=team)
		workout = Workout.objects.create(user=profile, name='Chest Day', description='Bench press')
		self.assertEqual(workout.name, 'Chest Day')
