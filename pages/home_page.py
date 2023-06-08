from selenium.webdriver.common.by import By
from Areg_Avetisyan_Exam.lib.helpers import Helpers


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
