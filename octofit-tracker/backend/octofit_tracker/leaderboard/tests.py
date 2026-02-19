from django.test import TestCase


from .models import Leaderboard
from users.models import Profile
from teams.models import Team
from django.contrib.auth.models import User
from django.test import TestCase

class LeaderboardModelTest(TestCase):
	def test_create_leaderboard(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team')
		profile = Profile.objects.create(user=user, team=team)
		leaderboard = Leaderboard.objects.create(user=profile, points=100)
		self.assertEqual(leaderboard.points, 100)
