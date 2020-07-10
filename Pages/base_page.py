import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.firefox.options import Options
        
#driver = Chrome()
#driver = Firefox()

browser_options = Options()
browser_options.add_argument("--headless")
browser_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote(
   command_executor='http://localhost:4444/wd/hub', 
   options=browser_options)


@pytest.fixture(scope="session")
def stp():
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def stp_home():
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/inventory.html")
    # yield driver
    # driver.quit()

@pytest.fixture()
def reload():
    driver.refresh()