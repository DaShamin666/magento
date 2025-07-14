import allure
from base.base_test import BaseTest


@allure.feature("тесты регистарции пользователя")
class TestRegistration(BaseTest):



    @allure.title("Регистрируемся(позитивный тест)")
    def test_registration(self):
        with allure.step("открываем страницу регистрации"):
            self.registration.open()
        with allure.step("вводим имя"):
            self.registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            self.registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            self.registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            self.registration.input_password('Qwerty12345')
        with allure.step("Вводим пароль повторно"):
            self.registration.input_confirm_password('Qwerty12345')
            assert self.registration.input_password == self.registration.input_confirm_password, f"пароли не совпадают"
        with allure.step("Нажимаем кнопку: 'create account'"):
            self.registration.click_button_confirm()
        with allure.step("аккаунт успешно создан"):
            success_message = self.registration.text_sucsses_create()
            expected_message = "Thank you for registering with Main Website Store."
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',"
                                                         f" но было: '{success_message}'")

    @allure.title("Регистрируемся(негативный тест Password Strength: Weak)")
    def test_registration_negativ(self):
        with allure.step("открываем страницу регистрации"):
            self.registration.open()
        with allure.step("вводим имя"):
            self.registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            self.registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            self.registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            self.registration.input_password('qwerty12345')
        with allure.step("Вводим пароль повторно"):
            self.registration.input_confirm_password('qwerty12345')
            assert self.registration.input_password == self.registration.input_confirm_password, f"пароли не совпадают"
        with allure.step("Нажимаем кнопку: 'create account'"):
            self.registration.click_button_confirm()
        with allure.step("слабый пароль"):
            success_message = self.registration.password_strength_weak()
            expected_message = "Weak"
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',"
                                                         f" но было: '{success_message}'")


    @allure.title("Регистрируемся(негативный тест Please enter the same value again)")
    def test_registration_enter_value_again(self):
        with allure.step("открываем страницу регистрации"):
            self.registration.open()
        with allure.step("вводим имя"):
            self.registration.input_firstname('daniil')
        with allure.step("вводим фамилию"):
            self.registration.input_lastname('shamin')
        with allure.step("Вводим почту"):
            self.registration.input_email('shamin@yan.ru')
        with allure.step("Вводим пароль"):
            self.registration.input_password('Qwerty12345')
        with allure.step("Вводим пароль повторно"):
            self.registration.input_confirm_password('qwerty12345')
            assert self.registration.input_password == self.registration.input_confirm_password, f"пароли не совпадают"
        with allure.step("Нажимаем кнопку: 'create account'"):
            self.registration.click_button_confirm()
        with allure.step("введите пароль еще раз"):
            success_message = self.registration.enter_value_again()
            expected_message = "Please enter the same value again."
            assert success_message == expected_message, (f"Ожидалось: '{expected_message}',"
                                                         f" но было: '{success_message}'")






