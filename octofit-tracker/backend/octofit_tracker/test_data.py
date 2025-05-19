# Test data for the octofit_db database

users = [
    {"email": "user1@example.com", "name": "User One", "age": 25},
    {"email": "user2@example.com", "name": "User Two", "age": 30},
    {"email": "user3@example.com", "name": "User Three", "age": 22},
]

teams = [
    {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
    {"name": "Team Beta", "members": ["user3@example.com"]},
]

activities = [
    {"activity_id": 1, "name": "Running", "calories_burned": 300},
    {"activity_id": 2, "name": "Cycling", "calories_burned": 400},
    {"activity_id": 3, "name": "Swimming", "calories_burned": 500},
]

leaderboard = [
    {"leaderboard_id": 1, "user": "user1@example.com", "points": 100},
    {"leaderboard_id": 2, "user": "user2@example.com", "points": 150},
    {"leaderboard_id": 3, "user": "user3@example.com", "points": 200},
]

workouts = [
    {"workout_id": 1, "user": "user1@example.com", "activity": "Running", "duration": 30},
    {"workout_id": 2, "user": "user2@example.com", "activity": "Cycling", "duration": 45},
    {"workout_id": 3, "user": "user3@example.com", "activity": "Swimming", "duration": 60},
]
