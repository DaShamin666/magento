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
        click_page.click()


    @allure.step("выбор одежды")
    def choise_tshort(self):
        click_page = self.driver.find_element(*self._CHOISE_SHMOT)
        actions = ActionChains(self.driver)
        actions.move_to_element(click_page).perform()


    @allure.step("выбор размера")
    def choose_size(self):
        click_size = self.driver.find_element(*self._CHOISE_SIZE)
        click_size.click()


    @allure.step("выбор цвета")
    def choose_color(self):
        choose_color_button = self.driver.find_element(*self._CHOISE_COLOR)
        choose_color_button.click()


    @allure.step("добавляем товар")
    def click_compair(self):
        compair_button = self.driver.find_element(*self._CLICK_TO_COMPAIR)
        compair_button.click()
