import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SportsTracker:

    def __init__(self, username: str, password: str):
        self.url = "https://www.sports-tracker.com"
        self.username = username
        self.password = password
        self.driver = None

    def list_all_workouts(self):
        self.driver = webdriver.Safari()
        self.driver.get(f"{self.url}/dashboard")
        username_textbox = self.driver.find_element_by_class_name("username")
        username_textbox.send_keys(self.username)
        password_textbox = self.driver.find_element_by_class_name("password")
        password_textbox.send_keys(self.password)
        submit_button = self.driver.find_element_by_class_name("submit")
        submit_button.click()
        feeds = self.driver.find_elements_by_class_name("feed-card")
        logging.info(len(feeds))
        for feed in feeds:
            logging.info(feed.text)
        self.driver.close()
        return [{'id': "5d8b460e17683adfb9b6240b"}]

    def workout_saveas_gpx(self, workout_id: str, output_path: str):
        self.driver = webdriver.Safari()
        self.driver.get(f"{self.url}/workout/{self.username}/{workout_id}")
        edit_button = self.driver.find_elements_by_class_name("workout-edit")
        logging.info(edit_button)
        self.driver.close()
        return 0
