import allure
from pages.sale import SalePage


class TestSale:
    def setup_method(self):
        self.sale = SalePage(self.driver)


    @allure.title("скидочки")
    def test_shopping(self):
        self.sale.open()
        self.sale.clicl_womens_deals()
        self.sale.choise_tshort()
        self.sale.choose_size()
        self.sale.choose_color()
        self.sale.click_compair()
