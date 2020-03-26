import pytest
from Pages.base_page import driver
from Pages.base_page import stp
from Pages.base_page import reload
from Pages.login_page import LoginPage
from Pages.home_page import HomePage

import time

@pytest.mark.usefixtures("stp", "reload")
class TestHomePage:
    lp = LoginPage()
    hp = HomePage()
    def testAddToCart(self):
        self.lp.set_username("standard_user")
        self.lp.set_password("secret_sauce")
        self.lp.login_button_click()
        self.hp.add_to_cart_from_home_page(1)
        self.hp.add_to_cart_from_home_page(3)
        self.hp.add_to_cart_from_home_page(5)
        self.hp.open_item()
        self.hp.add_to_cart_from_item()
        self.hp.back_to_home_page()

        assert self.hp.burger_menu_exist()
        assert self.hp.session_storage_is_full()