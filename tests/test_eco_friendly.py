import allure
from base.base_test import BaseTest


class TestChoiseShmot(BaseTest):

    @allure.title("Выбираем")
    def test_shopping(self):
        self.eco_friendly.open()
        self.eco_friendly.click_next()
        self.eco_friendly.acction_choose()
        self.eco_friendly.click_choose_size_xl()
        self.eco_friendly.click_choose_color_purple()
        self.eco_friendly.click_compair()
