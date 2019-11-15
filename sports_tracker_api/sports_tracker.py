from selenium import webdriver


class SportsTracker:

    def __init__(self, username: str, password: str):
        self.url = "https://www.sports-tracker.com"
        self.username = username
        self.driver = webdriver.Safari()
        self.driver.get(self.url)

    def list_all_workouts(self):
        return []

    def workout_saveas_gpx(self, workout_id: str, output_path: str):
        return 0
