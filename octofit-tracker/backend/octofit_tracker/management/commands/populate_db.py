from django.core.management.base import BaseCommand
from pymongo import MongoClient
from octofit_tracker.test_data import users, teams, activities, leaderboard, workouts

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Populate users
        db.users.insert_many(users)

        # Populate teams
        db.teams.insert_many(teams)

        # Populate activities
        db.activity.insert_many(activities)

        # Populate leaderboard
        db.leaderboard.insert_many(leaderboard)

        # Populate workouts
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
