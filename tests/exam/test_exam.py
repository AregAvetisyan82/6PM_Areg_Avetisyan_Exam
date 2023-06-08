import pytest
from Areg_Avetisyan_Exam.tests.exam.baseTest import BaseTest
from Areg_Avetisyan_Exam.testing_data import test_data


@pytest.mark.exam
class TestExam(BaseTest):
    def test_exam(self):
        self.navigate_to_free_shipping()
        self.get_text_from_page(test_data.text_to_check1)
        self.search_text_and_check_tags(test_data.searching_text, test_data.text_to_check2)
