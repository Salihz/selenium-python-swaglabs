from Pages.base_page import driver

class LoginPage:
    # locators
    user_name_id = "user-name"
    password_ld = "password"
    login_button_class = "btn_action"
    error_button_class = "error-button"

    # texts
    credentials_not_match_text = "Username and password do not match any user in this service"
    user_locked_out_text = "Sorry, this user has been locked out."

    # actions
    def set_username(self, username):
        el = driver.find_element_by_id(self.user_name_id)
        el.send_keys(username)

    def set_password(self, password):
        el = driver.find_element_by_id(self.password_ld)
        el.send_keys(password)

    def login_button_click(self):
        el = driver.find_element_by_class_name(self.login_button_class)
        el.click()

    # assertions
    def error_button_exist(self):
        return driver.find_element_by_class_name(self.error_button_class) != None

    def message_credentials_not_match_exist(self):
        return driver.find_element_by_xpath('//*[text()="' + self.credentials_not_match_text + '"]') != None

    def message_user_locked_out_exist(self):
        return driver.find_element_by_xpath('//*[text()="' + self.user_locked_out_text + '"]') != None

    def username_field_exist(self):
        return driver.find_element_by_id(self.user_name_id) != None
    
    def password_field_exist(self):
        return driver.find_element_by_id(self.password_ld) != None

    def login_button_exist(self):
        return driver.find_element_by_class_name(self.login_button_class) != None


