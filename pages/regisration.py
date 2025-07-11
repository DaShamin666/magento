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
        assert firstname_field.is_displayed(), "Поле для ввода имени не отображается"
        firstname_field.send_keys(firstname)


    @allure.step("Вводим фамилию")
    def input_lastname(self, lastname):
        lastname_field = self.driver.find_element(*self._LAST_NAME)
        assert lastname_field.is_displayed(), "Поле для ввода фамилии не отображается"
        lastname_field.send_keys(lastname)


    @allure.step("Вводим почту")
    def input_email(self, email):
        email_field = self.driver.find_element(*self._EMAIL)
        assert email_field.is_displayed(), "Поле для ввода почты не отображается"
        email_field.send_keys(email)


    @allure.step("Вводим пароль")
    def input_password(self, password):
        password_field = self.driver.find_element(*self._PASSWORD)
        assert password_field.is_displayed(), "Поле для ввода пароля не отображается"
        password_field.send_keys(password)


    @allure.step("Вводим пароль повторно")
    def input_confirm_password(self, confirm_password):
        confirm_password_field = self.driver.find_element(*self._CONFIRM_PASSWORD)
        assert confirm_password_field.is_displayed(), "Поле для повторного ввода пароля не отображается"
        confirm_password_field.send_keys(confirm_password)


    @allure.step("Нажимаем кнопку")
    def click_button_confirm(self):
        confirm_button = self.driver.find_element(*self._BUTTON_CONFIRM)
        assert confirm_button.is_displayed(), "Кнопка подтверждения не отображается"
        assert confirm_button.is_enabled(), "Кнопка подтверждения недоступна для нажатия"
        confirm_button.click()

