from django.test import TestCase


from .models import Team
from django.test import TestCase

class TeamModelTest(TestCase):
	def test_create_team(self):
		team = Team.objects.create(name='Avengers')
		self.assertEqual(team.name, 'Avengers')
