import time
from selenium.webdriver.common.by import By
from Areg_Avetisyan_Exam.lib.helpers import Helpers
from hamcrest import equal_to
from Areg_Avetisyan_Exam.lib.assertions import assert_that


class ExamPage(Helpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    shipping_and_delivery_txt = (By.XPATH, "//*[@data-page-id='shipping-and-returns']/h1")

    def get_text_of_heading(self, expected_result):
        actual_result = self.find(self.shipping_and_delivery_txt, get_text=True)
        assert_that(actual_result, equal_to(expected_result))

    def navigate_back(self):
        self.go_back()
