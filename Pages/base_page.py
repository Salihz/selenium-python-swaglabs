import pytest
from selenium.webdriver import Chrome
        
driver = Chrome()

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
    yield driver
    driver.quit()

@pytest.fixture()
def reload():
    driver.refresh()