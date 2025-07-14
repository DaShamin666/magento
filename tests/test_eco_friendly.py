import allure
from base.base_test import BaseTest

@allure.feature("Выбираем товар на странице eco-friendly ")
class TestChoiseShmot(BaseTest):

    @allure.title("выбираем товар, добавляем его в раздел сравнений")
    def test_shopping(self):
        with allure.step("открываем страницу выбора товара"):
            self.eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            self.eco_friendly.click_next()
        with allure.step("выбираем товар"):
            self.eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            self.eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            self.eco_friendly.click_choose_color_purple()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            self.eco_friendly.click_compair()
        with allure.step("проверяем что товар добавился"):
            quantity= self.eco_friendly.item_list()
            assert len(quantity) >= 1

    @allure.title("очищаем список сравнения")
    def clear_compair(self):
        with allure.step("открываем страницу выбора товара"):
            self.eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            self.eco_friendly.click_next()
        with allure.step("выбираем товар"):
            self.eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            self.eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            self.eco_friendly.click_choose_color_purple()
        with allure.step("нажимаем кнопку добавить в сравнение"):
            self.eco_friendly.click_compair()
        with allure.step("проверяем что товар добавился"):
            self.eco_friendly.item_list()
        with allure.step("очищаем список"):
            self.eco_friendly.click_clear_compair()

    @allure.title("добавляем товар в корзину")
    def add_to_cart(self):
        with allure.step("открываем страницу выбора товара"):
            self.eco_friendly.open()
        with allure.step("нажимаем кнопку перехода на следующую страницу"):
            self.eco_friendly.click_next()
        with allure.step("выбираем товар"):
            self.eco_friendly.acction_choose()
        with allure.step("выбираем размер"):
            self.eco_friendly.click_choose_size_xl()
        with allure.step("выбираем цвет"):
            self.eco_friendly.click_choose_color_purple()
        with allure.step("добавляем товар в корзину"):
            self.eco_friendly.click_add_to_cart()
        with allure.step("проверяем что товар появился в корзине"):
            cart = self.eco_friendly.cart_changed()
            assert len(cart) >= 1

