import logging
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options


class SportsTracker:

    def __init__(self, username: str, password: str):
        self.url = "https://www.sports-tracker.com"
        self.username = username
        self.password = password
        options = Options()
        options.add_argument('--browser.helperApps.neverAsk.saveToDisk=application/octet-stream')
        prefs = {'download.default_directory': 'data'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome('/Users/ftrojan/lib/chromedriver/chromedriver', options=options)

    def list_dashboard_workouts(self):
        self.driver.get(f"{self.url}/diary/workout-list")
        sessionkey = {}
        try:
            element = WebDriverWait(self.driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "username"))
            )
            element.send_keys(self.username)
            self.driver.find_element_by_class_name("password").send_keys(self.password)
            self.driver.find_element_by_class_name("submit").send_keys(Keys.RETURN)
            try:
                WebDriverWait(self.driver, 10).until(
                    ec.presence_of_element_located((By.CLASS_NAME, "diary-list__workouts"))
                )
                ul = self.driver.find_element_by_tag_name("ul")
                feeds = ul.find_elements_by_tag_name("li")
                logging.info(len(feeds))
                workouts = []
                for feed in feeds:
                    link = feed.find_element_by_tag_name("a")
                    workout = {
                        'link': link.get_attribute("href")
                    }
                    workouts.append(workout)
                    logging.info(workout)
            except:
                workouts = []
            sessionkey = self.driver.get_cookie("sessionkey")
            logging.info(f"sessionkey={sessionkey}")
        except:
            logging.error("error happened")
        return workouts, sessionkey

    def workouts_saveas_gpx(self, output_path: str):
        # inspired by https://gist.github.com/devalls/f82eaaa6d3b7f15a1c16fbdc388eb88e
        workouts, sessionkey = self.list_dashboard_workouts()
        for workout in workouts:
            wid = workout['link'].split('/')[-1]
            token = sessionkey['value']
            url = f"http://www.sports-tracker.com/apiserver/v1/workout/exportGpx/{wid}?token={token}"
            outfile = f"{output_path}/SportsTracker-{wid}.gpx"
            logging.info(f"url={url} to be saved as {outfile}")
            self.driver.get(url)
        # self.driver.get(workouts[0]['link'])
        # edit_button = WebDriverWait(self.driver, 10).until(
        #     ec.presence_of_element_located((By.CLASS_NAME, "workout-edit"))
        # )
        # logging.info(edit_button)
        self.driver.close()
        return 0
