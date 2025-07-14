from lib2to3.pgen2 import driver

from selenium.webdriver.chrome.webdriver import WebDriver
from meta_classes.meta_locators import MetaLocator
from selenium.webdriver.support.ui import WebDriverWait
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class BasePage(metaclass=MetaLocator):
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self._PAGE_URL)

    def find_element(self, locator):
        """Найти элемент с явным ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Нажать на элемент с явным ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)


    def attach_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к отчету Allure."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def action_choose(self, locator):
        """Выбор элемента с проверкой его видимости и выполнением действия наведения."""
        action_element = self.find_element(locator)  # Находим элемент с явным ожиданием
        actions = ActionChains(self.driver)
        actions.move_to_element(action_element).perform()

    def allert_confirm(self):
        """принимаем попап"""
        alert = self.driver._switch_to.alert
        alert.accept()
