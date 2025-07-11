from pages.eco_friendly import EcoFriendlyPage
from pages.regisration import RegistrationPage
from pages.sale import SalePage


class BaseTest:

    def setup_method(self):
        self.eco_friendly = EcoFriendlyPage(self.driver)
        self.registration = RegistrationPage(self.driver)
        self.sale = SalePage(self.driver)

