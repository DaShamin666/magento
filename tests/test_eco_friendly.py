import allure
from pages.eco_friendly import EcoFriendlyPage


class TestChoiseShmot:
    def setup_method(self):
        self.eco_friendly = EcoFriendlyPage(self.driver)


    @allure.title("Выбираем")
    def test_shopping(self):
        self.eco_friendly.open()
        self.eco_friendly.click_next()
        self.eco_friendly.click_choose()
        self.eco_friendly.click_choose_size()
        self.eco_friendly.click_choose_color()
        self.eco_friendly.click_compair()
