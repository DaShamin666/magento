from base.base_page import BasePage
import allure
from selenium.webdriver.common.action_chains import ActionChains


class SalePage(BasePage):
    _PAGE_URL = 'https://magento.softwaretestingboard.com/promotions/women-sale.html'

    _WOMENS_DEALS = "//a[@class='block-promo sale-main' and .//span[@class='info' and text()='Women’s Deals']]"
    _CHOISE_SHMOT = "//img[@class='product-image-photo' and @alt='Breathe-Easy Tank']"
    _CHOISE_SIZE = "//div[@class='swatch-option text' and @option-label='S']"
    _CHOISE_COLOR = "//div[@class='swatch-option color' and @option-label='Yellow']"
    _CLICK_TO_COMPAIR = "//a[@class='action tocompare' and @title='Add to Compare']"

    @allure.step("переход к разделу с вуменс сеил")
    def clicl_womens_deals(self):
        click_page = self.driver.find_element(*self._WOMENS_DEALS)
        assert click_page.is_displayed(), "Ссылка на раздел 'Women's Deals' не отображается"
        click_page.click()


    @allure.step("выбор одежды")
    def choise_tshort(self):
        click_page = self.driver.find_element(*self._CHOISE_SHMOT)
        assert click_page.is_displayed(), "Элемент одежды не отображается"
        actions = ActionChains(self.driver)
        actions.move_to_element(click_page).perform()


    @allure.step("выбор размера")
    def choose_size_s(self):
        click_size = self.driver.find_element(*self._CHOISE_SIZE)
        assert click_size.is_displayed(), "Кнопка выбора размера не отображается"
        click_size.click()


    @allure.step("выбор цвета")
    def choose_color_yellow(self):
        choose_color_button = self.driver.find_element(*self._CHOISE_COLOR)
        assert choose_color_button.is_displayed(), "Кнопка выбора цвета не отображается"
        choose_color_button.click()


    @allure.step("добавляем товар")
    def click_compair(self):
        compare_button = self.driver.find_element(*self._CLICK_TO_COMPAIR)
        assert compare_button.is_displayed(), "Кнопка 'Добавить к сравнению' не отображается"
        compare_button.click()
