from Pages.base_page import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class HomePage:
    # locators
    burger_menu_class = "bm-burger-button"
    shopping_cart_class = "shopping_cart_container"
    logout_button_id = "logout_sidebar_link"
    reset_app_button_id = "reset_sidebar_link"
    shopping_cart_num_class = "fa-layers-counter shopping_cart_badge"
    x_button_class = "bm-cross-button"

    # methods
   
    def burger_menu_exist(self):
        return driver.find_element_by_class_name(self.burger_menu_class) != None

    def shopping_cart_exist(self):
        return driver.find_element_by_class_name(self.shopping_cart_class) != None

    def burger_menu_open(self):
        el = driver.find_element_by_class_name(self.burger_menu_class)
        el.click()

    def logout_button_click(self):
        el = driver.find_element_by_id(self.logout_button_id)
        WebDriverWait(driver, timeout=3).until(expected_conditions.element_to_be_clickable((By.ID, self.logout_button_id)))
        el.click()

    def reset_app_button_click(self):
        el = driver.find_element_by_id(self.reset_app_button_id)
        WebDriverWait(driver, timeout=3).until(expected_conditions.element_to_be_clickable((By.ID, self.reset_app_button_id)))
        el.click()

    def shopping_cart_num_exist(self):
        # return driver.find_element_by_class_name(self.shopping_cart_num_class) != None
        return driver.find_element_by_xpath('//*[@id="shopping_cart_container"]/a/span') != None
        
    
    def x_button_click(self):
        el = driver.find_element_by_class_name(self.x_button_class)
        WebDriverWait(driver, timeout=3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, self.x_button_class)))
        el.click()