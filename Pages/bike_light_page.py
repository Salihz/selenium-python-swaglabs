from Pages.base_page import driver

class BikeLightPage:
    # locators
    add_to_cart_button_xpath = '//*[@class="inventory_details_desc_container"]//button'
    back_button_xpath = '//*[@class="inventory_details"]/button'

    # actions
    def add_to_cart_from_item(self):
        el = driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        el.click()

    def remove_from_cart_item(self):
        el = driver.find_element_by_xpath(self.add_to_cart_button_xpath)
        el.click()

    def back_to_home_page(self):
        el = driver.find_element_by_xpath(self.back_button_xpath)
        el.click()

