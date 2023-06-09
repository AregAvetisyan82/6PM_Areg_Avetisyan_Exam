from selenium.webdriver.common.by import By
from Areg_Avetisyan_Exam.lib.helpers import Helpers
from hamcrest import equal_to
from Areg_Avetisyan_Exam.lib.assertions import assert_that


class HomePage(Helpers):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    free_shipping_link = (By.XPATH, "(//*[@href='/shipping-and-delivery-questions'])[1]")
    search_input = (By.ID, "searchAll")
    search_btn = (By.XPATH, "//*[@type='submit']")
    tag_clothing = (By.XPATH, "(//*[@data-singleselect='true'])[1]")
    tag_dresses = (By.XPATH, "(//*[@data-singleselect='true'])[2]")

    def click_on_free_shipping(self):
        self.find_and_click(self.free_shipping_link)

    def search_data_and_check_tags(self, text_to_search, expected_result: list):
        self.find_and_send_keys(self.search_input, text_to_search)
        self.find_and_click(self.search_btn)
        clothes = self.find(self.tag_clothing, get_text=True)
        dresses = self.find(self.tag_dresses, get_text=True)
        actual_result = [clothes, dresses]
        assert_that(actual_result, equal_to(expected_result))
