from base.base_page import BasePage
import allure
from selenium.webdriver.common.action_chains import ActionChains
import allure




class EcoFriendlyPage(BasePage):
    _PAGE_URL = 'https://magento.softwaretestingboard.com/collections/eco-friendly.html'

    _BUTTON_NEXT = "//a[@class='action next' and @title='Next' and contains(span/text(), 'Next')]"
    _CHOISE_SHMOT = "//img[@class='product-image-photo' and contains(@src, 'mj06-blue_main_1.jpg')]"
    _CHOISE_SIZE = "//div[@class='swatch-option text' and @option-id='170' and @aria-label='XL']"
    _CHOISE_COLOR = ("//div[@class='swatch-option color selected'"
                     " and @option-id='57' and @aria-checked='true']")
    _CLICK_TO_COMPAIR = "//a[span[text()='Add to Compare']]"

    @allure.step("нажать кнопку далее")
    def click_next(self):
        click_button = self.driver.find_element(*self._BUTTON_NEXT)
        assert click_button.is_displayed(), "Кнопка 'Далее' не отображается"
        click_button.click()


    @allure.step("выбор одежды")
    def acction_choose(self):
        action_element = self.driver.find_element(*self._CHOISE_SHMOT)
        assert action_element.is_displayed(), "Элемент одежды не отображается"
        actions = ActionChains(self.driver)
        actions.move_to_element(action_element).perform()


    @allure.step("выбор размера")
    def click_choose_size_xl(self):
        choose_size_button = self.driver.find_element(*self._CHOISE_SIZE)
        assert choose_size_button.is_displayed(), "Кнопка выбора размера не отображается"
        choose_size_button.click()


    @allure.step("выбор цвета")
    def click_choose_color_purple(self):
        choose_color_button = self.driver.find_element(*self._CHOISE_COLOR)
        assert choose_color_button.is_displayed(), "Кнопка выбора цвета не отображается"
        choose_color_button.click()


    @allure.step("добавляем товар")
    def click_compair(self):
        compair_button = self.driver.find_element(*self._CLICK_TO_COMPAIR)
        assert compair_button.is_displayed(), "Кнопка 'Добавить к сравнению' не отображается"
        compair_button.click()