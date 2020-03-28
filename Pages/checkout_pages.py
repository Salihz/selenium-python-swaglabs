from Pages.base_page import driver

class CheckoutPages:
    # locators

    checkout_button_xpath = '//*[@class="cart_footer"]/a[2]'
    first_name_id = 'first-name'
    last_name_id = 'last-name'
    postal_code_id = 'postal-code'
    continue_button_xpath = '//*[@class="checkout_buttons"]/input'

    first_name = "Hernan"
    last_name = "Cattaneo"
    postal_code = "21000"

    order_dispatched_text = 'Your order has been dispatched, and will arrive just as fast as the pony can get there!'

    # actions

    def checkout_button_click(self):
        el = driver.find_element_by_xpath(self.checkout_button_xpath)
        el.click()

    def fill_out_first_name(self):
        el = driver.find_element_by_id(self.first_name_id)
        el.send_keys(self.first_name)

    def fill_out_last_name(self):
        el = driver.find_element_by_id(self.last_name_id)
        el.send_keys(self.last_name)

    def fill_out_postal_code(self):
        el = driver.find_element_by_id(self.postal_code_id)
        el.send_keys(self.postal_code)

    def continue_button_click(self):
        el = driver.find_element_by_xpath(self.continue_button_xpath)
        el.click()

    def finish_button_click(self):
        el = driver.find_element_by_xpath(self.checkout_button_xpath)
        el.click()

    def check_success_message(self):
        return driver.find_element_by_xpath('//*[text()="' + self.order_dispatched_text + '"]') != None
