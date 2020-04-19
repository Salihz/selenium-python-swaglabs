# selenium-python-swaglabs

This is a sample project with Selenium tests for [SwagLabs] website.  
Tools used for this project are: 
- Selenium (Python): https://www.selenium.dev/
- PyTest: https://docs.pytest.org/en/latest/

## Installation
Python: https://www.python.org/downloads/  
Selenium Libraries: https://www.selenium.dev/documentation/en/selenium_installation/installing_selenium_libraries/  
WebDriver binaries (Chrome): https://www.selenium.dev/documentation/en/webdriver/driver_requirements/#quick-reference   
PyTest: https://docs.pytest.org/en/latest/getting-started.html

## How to run tests
Tests can be ran using one of the following commands:  

```pytest``` - run the whole test suite  
```pytest .\Tests\test_cart.py``` - run tests within the specified file  
```pytest .\Tests\test_cart.py -k 'testAddToCart'``` - run the specific test  


[SwagLabs]: <https://www.saucedemo.com/>
