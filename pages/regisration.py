from base.base_page import BasePage
import allure


class RegistrationPage(BasePage):
    _PAGE_URL = 'https://magento.softwaretestingboard.com/customer/account/create/'

    _FIRST_NAME = "//input[@id='firstname' and contains(@class, 'input-text')]"
    _LAST_NAME = "//input[@id='lastname' and contains(@class, 'input-text')]"
    _EMAIL = "//input[@id='email_address' and contains(@class, 'input-text')]"
    _PASSWORD = "//input[@id='password' and contains(@class, 'input-text')]"
    _CONFIRM_PASSWORD = "//input[@id='password-confirmation' and contains(@class, 'input-text')]"
    _BUTTON_CONFIRM = ("//button[contains(@class, 'action submit primary')"
                       " and @title='Create an Account']")


    @allure.step("Вводим имя")
    def input_firstname(self, firstname):
        firstname_field = self.driver.find_element(*self._FIRST_NAME)
        firstname_field.send_keys(firstname)


    @allure.step("Вводим фамилию")
    def input_lastname(self, lastname):
        lastname_field = self.driver.find_element(*self._LAST_NAME)
        lastname_field.send_keys(lastname)


    @allure.step("Вводим почту")
    def input_email(self, email):
        email_field = self.driver.find_element(*self._EMAIL)
        email_field.send_keys(email)


    @allure.step("Вводим пароль")
    def input_password(self, password):
        password_field = self.driver.find_element(*self._PASSWORD)
        password_field.send_keys(password)


    @allure.step("Вводим пароль повторно")
    def input_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(*self._CONFIRM_PASSWORD)
        confirm_password_field.send_keys(confirm_password)


    @allure.step("Нажимаем кнопку")
    def click_button_confirm(self):
        self.driver.find_element(*self._BUTTON_CONFIRM).click()

