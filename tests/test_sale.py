import allure
from base.base_test import BaseTest


@allure.feature("Тесты раздела Sale")
class TestSale(BaseTest):



    @allure.title("очищаем список сравнения")
    def test_clear_compair(self):
        with allure.step("открываем страницу выбора товара"):
            self.sale.open()
        with allure.step("выбираем товар"):
            self.sale.choise_tshort()
        with allure.step("выбираем размер"):
            self.sale.choose_size_s()
        with allure.step("выбираем цвет"):
            self.sale.choose_color_yellow()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            self.sale.click_compair()
        with allure.step("проверяем что товар добавился"):
            self.sale.item_list()
        with allure.step("очищаем список"):
            self.sale.click_clear_compair()

    @allure.title("добавляем товар в корзину")
    def test_add_to_cart(self):
        with allure.step("открываем страницу выбора товара"):
            self.sale.open()
        with allure.step("выбираем товар"):
            self.sale.choise_tshort()
        with allure.step("выбираем размер"):
            self.sale.choose_size_s()
        with allure.step("выбираем цвет"):
            self.sale.choose_color_yellow()
        with allure.step("добавляем товар в корзину"):
            self.sale.click_add_to_cart()
        with allure.step("проверяем что товар появился в корзине"):
            cart = self.sale.cart_changed()
            assert len(cart) >= 1

    @allure.title("выбираем товар, добавляем его в раздел сравнений")
    def test_shopping(self):
        allure.step("открываем страницу выбора товара")
        self.sale.open()
        allure.step("выбираем товар")
        self.sale.choise_tshort()
        allure.step("выбираем размер")
        self.sale.choose_size_s()
        allure.step("выбираем цвет")
        self.sale.choose_color_yellow()
        allure.step("нажимаем кнопку добавить в сравнение")
        self.sale.click_compair()
        allure.step("проверяем что товар добавился")
        quantity = self.sale.item_list()
        assert len(quantity) >= 1

