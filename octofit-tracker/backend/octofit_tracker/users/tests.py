from django.test import TestCase


from django.contrib.auth.models import User
from .models import Profile
from teams.models import Team

class ProfileModelTest(TestCase):
	def test_create_profile(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team')
		profile = Profile.objects.create(user=user, team=team)
		self.assertEqual(profile.user.username, 'testuser')
		self.assertEqual(profile.team.name, 'Test Team')
