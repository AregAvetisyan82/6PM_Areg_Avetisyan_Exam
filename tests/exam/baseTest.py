import pytest


@pytest.mark.usefixtures("get_driver")
class BaseTest:
    def navigate_to_free_shipping(self):
        self.home_page.click_on_free_shipping()

    def get_text_from_page(self, expected_result):
        self.exam_page.get_text_of_heading(expected_result)

    def navigate_back_to_home(self):
        self.exam_page.navigate_back()

    def search_text_and_check_tags(self, text_to_search, expected_result):
        self.home_page.search_data_and_check_tags(text_to_search, expected_result)
