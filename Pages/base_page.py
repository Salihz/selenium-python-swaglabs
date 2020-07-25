import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import time
import os
from selenium.webdriver.firefox.options import Options
        
driver = Chrome()
#driver = Firefox()

browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-dev-shm-usage")

'''
driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub', 
   options=browser_options)
'''


@pytest.fixture(scope="session")
def stp(request):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    failed_before = request.session.testsfailed

    yield driver
    if request.session.testsfailed != failed_before:
        take_screenshot(driver)
    driver.quit()


@pytest.fixture(scope="session")
def stp_home(request):
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/inventory.html")
    failed_before = request.session.testsfailed

    yield driver
    if request.session.testsfailed != failed_before:
        take_screenshot(driver)
    driver.quit()


@pytest.fixture()
def reload():
    driver.refresh()


def take_screenshot(browser):
    ts = time.time()
    test_name = datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    if not os.path.exists("Screenshots"):
        os.mkdir("Screenshots")
    screenshots_dir = "Screenshots"
    screenshot_file_path = "{}/{}.png".format(screenshots_dir, test_name)
    browser.save_screenshot(
        screenshot_file_path
    )
