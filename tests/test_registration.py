import allure
from pages.regisration import RegistrationPage


class TestRegistration:
    def setup_method(self):
        self.registration = RegistrationPage(self.driver)


    @allure.title("Регистрируемся")
    def test_registration(self):
        self.registration.open()
        self.registration.input_firstname("Daniil")
        self.registration.input_lastname("Shamin")
        self.registration.input_email("shamin@milo33.ru")
        self.registration.input_password("123456d")
        self.registration.input_confirm_password("123456d")
        self.registration.click_button_confirm()
