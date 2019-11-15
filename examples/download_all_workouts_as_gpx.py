from sports_tracker_api.sports_tracker import SportsTracker

out_dir = "data"
tracker = SportsTracker(
    username="ftrojan",
    password="",
)
workouts = tracker.list_all_workouts()
for i, workout in enumerate(workouts):
    tracker.workout_saveas_gpx(workout.id, f"{out_dir}/workout{i:.3d}.gpx")
