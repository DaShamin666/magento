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
    _ITEM_LIST = "//strong[@id='block-compare-heading' and text()='Compare Products']"
    _ITEM_COUNT = "//span[@class='counter qty' and text()='1 item']"
    _CLICK_CLEAR_COMPAIR = "//a[@id='compare-clear-all' and contains(span/text(), 'Clear All')]"
    _CLICK_ADD_TO_CART = "//button[@title='Add to Cart' and contains(@class, 'action tocart primary') and span[text()='Add to Cart']]"
    _CART = "//span[@class='counter qty' and span[@class='counter-number' and text()]]"

    def clicl_womens_deals(self):
        self.click_element(*self._WOMENS_DEALS)


    def choise_tshort(self):
        self.action_choose(*self._CHOISE_SHMOT)


    def choose_size_s(self):
        self.click_element(*self._CHOISE_SIZE)


    def choose_color_yellow(self):
        self.click_element(*self._CHOISE_COLOR)


    def click_compair_to_womens(self):
        self.click_element(*self._CLICK_TO_COMPAIR)

    def click_compair(self):
        self.click_element(*self._CLICK_TO_COMPAIR)

    def item_list(self):
        items = self.find_element(*self._ITEM_LIST)
        items_count = len(items.find_elements(*self._ITEM_COUNT))
        return items_count

    def click_clear_compair(self):
        self.click_element(*self._CLICK_CLEAR_COMPAIR)
        self.allert_confirm()

    def click_add_to_cart(self):
        self.click_element(*self._CLICK_ADD_TO_CART)

    def cart_changed(self):
        return self.find_element(*self._CART).text


