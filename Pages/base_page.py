import pytest
from selenium.webdriver import Chrome
        
driver = Chrome()

@pytest.fixture(scope="session")
def stp():
    driver.maximize_window()
    driver.get("https://www.saucedemo.com")
    yield driver
    driver.quit()

@pytest.fixture()
def reload():
    driver.refresh()