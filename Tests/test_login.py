import pytest
from Pages.base_page import driver
from Pages.base_page import stp
from Pages.base_page import reload
from Pages.login_page import LoginPage
from Pages.home_page import HomePage


@pytest.mark.usefixtures("stp", "reload")
class TestloginPage:
    lp = LoginPage()
    hp = HomePage()
    # @pytest.mark.skip(reason="no way of currently testing this")
    def testInvalidLogin(self):
        self.lp.set_username("standard_user")
        self.lp.set_password("wrong_pass")
        self.lp.login_button_click()
        assert self.lp.error_button_exist()
        assert self.lp.message_credentials_not_match_exist()

    # @pytest.mark.skip(reason="no way of currently testing this")
    def testLockedOutLogin(self):
        self.lp.set_username("locked_out_user")
        self.lp.set_password("secret_sauce")
        self.lp.login_button_click()
        assert self.lp.error_button_exist()
        assert self.lp.message_user_locked_out_exist()

    # @pytest.mark.skip(reason="no way of currently testing this")
    def testValidLogin(self):
        self.lp.set_username("standard_user")
        self.lp.set_password("secret_sauce")
        self.lp.login_button_click()
        assert self.hp.burger_menu_exist()
        assert self.hp.shopping_cart_exist()

