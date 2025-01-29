import logging
import yaml
from sports_tracker_api.sports_tracker import SportsTracker

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%dT%H:%M:%S",
    format="%(asctime)s - %(levelname)s - %(module)s.%(funcName)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
    ],
)

out_dir = "data"
with open("data/secrets.yaml") as file:
    secrets = yaml.safe_load(file)
tracker = SportsTracker(
    username=secrets['username'],
    password=secrets['password'],
)
workouts = tracker.workouts_saveas_gpx(out_dir)
