from django.core.management.base import BaseCommand
from users.models import User
from teams.models import Team
from activities.models import Activity
from leaderboard.models import Leaderboard
from workouts.models import Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel')
        dc = Team.objects.create(name='Team DC')

        # Create Users
        tony = User.objects.create(username='ironman', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(username='captainamerica', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(username='hulk', email='bruce@marvel.com', team=marvel)
        clark = User.objects.create(username='superman', email='clark@dc.com', team=dc)
        brucew = User.objects.create(username='batman', email='bruce@dc.com', team=dc)
        diana = User.objects.create(username='wonderwoman', email='diana@dc.com', team=dc)

        # Create Activities
        Activity.objects.create(user=tony, type='run', duration=30, distance=5)
        Activity.objects.create(user=steve, type='cycle', duration=60, distance=20)
        Activity.objects.create(user=bruce, type='swim', duration=45, distance=2)
        Activity.objects.create(user=clark, type='run', duration=25, distance=6)
        Activity.objects.create(user=brucew, type='cycle', duration=50, distance=18)
        Activity.objects.create(user=diana, type='swim', duration=40, distance=3)

        # Create Workouts
        Workout.objects.create(user=tony, name='Chest Day', description='Bench press and flys')
        Workout.objects.create(user=steve, name='Leg Day', description='Squats and lunges')
        Workout.objects.create(user=bruce, name='Back Day', description='Pull-ups and rows')
        Workout.objects.create(user=clark, name='Speed Day', description='Sprints and agility')
        Workout.objects.create(user=brucew, name='Strength Day', description='Deadlifts and presses')
        Workout.objects.create(user=diana, name='Power Day', description='Clean and jerk')

        # Create Leaderboard entries
        Leaderboard.objects.create(user=tony, points=100)
        Leaderboard.objects.create(user=steve, points=90)
        Leaderboard.objects.create(user=bruce, points=80)
        Leaderboard.objects.create(user=clark, points=110)
        Leaderboard.objects.create(user=brucew, points=95)
        Leaderboard.objects.create(user=diana, points=105)

        self.stdout.write(self.style.SUCCESS('Successfully populated octofit_db with test data.'))
