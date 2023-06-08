from selenium.webdriver.common.by import By
from Areg_Avetisyan_Exam.lib.helpers import Helpers
from hamcrest import equal_to
from Areg_Avetisyan_Exam.lib.assertions import assert_that


class ExamPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
