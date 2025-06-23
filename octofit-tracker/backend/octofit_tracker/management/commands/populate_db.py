from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Users
        user1 = User.objects.create(email="alice@example.com", name="Alice", password="pass1")
        user2 = User.objects.create(email="bob@example.com", name="Bob", password="pass2")
        user3 = User.objects.create(email="carol@example.com", name="Carol", password="pass3")

        # Teams
        team1 = Team.objects.create(name="Red Rockets")
        team2 = Team.objects.create(name="Blue Blazers")

        # Activities
        Activity.objects.create(user=user1, activity_type="run", duration=30)
        Activity.objects.create(user=user2, activity_type="walk", duration=45)
        Activity.objects.create(user=user3, activity_type="strength", duration=20)

        # Leaderboard
        Leaderboard.objects.create(team=team1, points=120)
        Leaderboard.objects.create(team=team2, points=95)

        # Workouts
        Workout.objects.create(user=user1, workout_type="cardio", details={"sets": 3})
        Workout.objects.create(user=user2, workout_type="strength", details={"reps": 10})
        Workout.objects.create(user=user3, workout_type="flexibility", details={"minutes": 15})

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
