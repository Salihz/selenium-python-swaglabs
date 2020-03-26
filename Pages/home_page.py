from Pages.base_page import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class HomePage:
    # locators
    burger_menu_class = "bm-burger-button"
    shopping_cart_class = "shopping_cart_container"
    logout_button_id = "logout_sidebar_link"
    reset_app_button_id = "reset_sidebar_link"
    shopping_cart_num_xpath = '//*[@id="shopping_cart_container"]/a/span'
    x_button_class = "bm-cross-button"
    about_button_id = "about_sidebar_link"
    bike_light_id = "item_0_title_link"
    add_to_cart_button_xpath = '//*[@class="inventory_details_desc_container"]//button'
    back_button_xpath = '//*[@class="inventory_details"]/button'
    
    about_url = "https://saucelabs.com/"

    # actions
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
    
    def x_button_click(self):
        el = driver.find_element_by_class_name(self.x_button_class)
        WebDriverWait(driver, timeout=3).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, self.x_button_class)))
        el.click()

    def about_button_click(self):
        el = driver.find_element_by_id(self.about_button_id)
        WebDriverWait(driver, timeout=3).until(expected_conditions.element_to_be_clickable((By.ID, self.about_button_id)))
        el.click()

    def add_to_cart_from_home_page(self, n):
        el = driver.find_element_by_xpath('//*[@class="inventory_item"][' + str(n) + ']//button')
        el.click()

    def open_item(self):
        el = driver.find_element_by_id(self.bike_light_id)
        el.click()

    def add_to_cart_from_item(self):
        el = driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        el.click()

    def back_to_home_page(self):
        el = driver.find_element_by_xpath(self.back_button_xpath)
        el.click()



    # assertions
    def burger_menu_exist(self):
        return driver.find_element_by_class_name(self.burger_menu_class) != None

    def shopping_cart_exist(self):
        return driver.find_element_by_class_name(self.shopping_cart_class) != None

    def shopping_cart_num_exist(self):
        try:
            driver.find_element_by_xpath(self.shopping_cart_num_xpath)
            return False
        except NoSuchElementException:
            return True
        
    def session_storage_is_empty(self):
        return driver.execute_script('return window.sessionStorage.getItem("cart-contents")') == None

    def session_storage_is_full(self):
        return driver.execute_script('return window.sessionStorage.getItem("cart-contents")') == '[4,1,2,0]'

    def check_about_url(self):
        if(driver.current_url == self.about_url):
            return True
        else:
            return False
