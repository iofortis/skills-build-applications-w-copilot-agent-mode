from django.test import TestCase


from .models import Activity
from users.models import Profile
from teams.models import Team
from django.contrib.auth.models import User
from django.test import TestCase

class ActivityModelTest(TestCase):
	def test_create_activity(self):
		user = User.objects.create(username='testuser')
		team = Team.objects.create(name='Test Team')
		profile = Profile.objects.create(user=user, team=team)
		activity = Activity.objects.create(user=profile, type='run', duration=30, distance=5)
		self.assertEqual(activity.type, 'run')
