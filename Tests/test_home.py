import pytest
from Pages.base_page import driver
from Pages.base_page import stp_home
from Pages.base_page import reload
from Pages.login_page import LoginPage
from Pages.home_page import HomePage

@pytest.mark.usefixtures("stp_home", "reload")
class TestHomePage:
    lp = LoginPage()
    hp = HomePage()
    def testResetAppState(self):
        driver.execute_script('window.sessionStorage.setItem("cart-contents","[4,0,1]")')
        self.hp.burger_menu_open()
        self.hp.reset_app_button_click()
        self.hp.x_button_click()

        assert self.hp.shopping_cart_num_exist()
        assert self.hp.session_storage_is_empty()

    def testLogout(self):
        self.hp.burger_menu_open()
        self.hp.logout_button_click()

        assert self.lp.username_field_exist()
        assert self.lp.password_field_exist()
        assert self.lp.login_button_exist()

    def testAbout(self):
         driver.get("https://www.saucedemo.com/inventory.html")
         self.hp.burger_menu_open()
         self.hp.about_button_click()
         
         assert self.hp.check_about_url()

        
