from base.base_page import BasePage



class EcoFriendlyPage(BasePage):
    _PAGE_URL = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    _BUTTON_NEXT = "//a[@class='action next' and @title='Next' and contains(span/text(), 'Next')]"
    _CHOISE_SHMOT = "//img[@class='product-image-photo' and contains(@src, 'mj06-blue_main_1.jpg')]"
    _CHOISE_SIZE = "//div[@class='swatch-option text' and @option-id='170' and @aria-label='XL']"
    _CHOISE_COLOR = ("//div[@class='swatch-option color selected'"
                     " and @option-id='57' and @aria-checked='true']")
    _CLICK_TO_COMPAIR = "//a[span[text()='Add to Compare']]"
    _ITEM_LIST = "//strong[@id='block-compare-heading' and text()='Compare Products']"
    _ITEM_COUNT = "//span[@class='counter qty' and text()='1 item']"
    _CLICK_CLEAR_COMPAIR ="//a[@id='compare-clear-all' and contains(span/text(), 'Clear All')]"
    _CLICK_ADD_TO_CART = "//button[@title='Add to Cart' and contains(@class, 'action tocart primary') and span[text()='Add to Cart']]"
    _CART = "//span[@class='counter qty' and span[@class='counter-number' and text()]]"

    def click_next(self):
        self.click_element(*self._BUTTON_NEXT)


    def acction_choose(self):
        action_element = self.action_choose(*self._CHOISE_SHMOT)
        assert action_element.is_displayed()



    def click_choose_size_xl(self):
        self.click_element(*self._CHOISE_SIZE)


    def click_choose_color_purple(self):
        self.click_element(*self._CHOISE_COLOR)


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