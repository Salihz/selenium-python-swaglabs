import pytest
from Pages.base_page import driver
from Pages.base_page import stp
from Pages.base_page import reload
from Pages.login_page import LoginPage
from Pages.home_page import HomePage
from Pages.bike_light_page import BikeLightPage

import time

@pytest.mark.usefixtures("stp", "reload")
class TestShopping:
    lp = LoginPage()
    hp = HomePage()
    blp = BikeLightPage()

    def testAddToCart(self):
        self.lp.set_username("standard_user")
        self.lp.set_password("secret_sauce")
        self.lp.login_button_click()
        self.hp.add_to_cart_from_home_page(1)
        self.hp.add_to_cart_from_home_page(3)
        self.hp.add_to_cart_from_home_page(5)
        self.hp.open_item()
        self.blp.add_to_cart_from_item()
        self.blp.back_to_home_page()

        assert self.hp.burger_menu_exist()
        assert self.hp.session_storage_is_full()

    def testRemoveFromCart(self):
        driver.execute_script('window.sessionStorage.setItem("cart-contents","[4,0,1]")')
        self.hp.remove_from_cart_home_page(1)
        self.hp.remove_from_cart_home_page(3)
        self.hp.open_item()
        self.blp.remove_from_cart_item()
        self.blp.back_to_home_page()

        assert self.hp.burger_menu_exist()
        assert self.hp.shopping_cart_num_exist()