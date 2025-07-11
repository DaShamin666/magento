import allure
from base.base_test import BaseTest


class TestSale(BaseTest):

    @allure.title("скидочки")
    def test_shopping(self):
        self.sale.open()
        self.sale.clicl_womens_deals()
        self.sale.choise_tshort()
        self.sale.choose_size_s()
        self.sale.choose_color_yellow()
        self.sale.click_compair()
