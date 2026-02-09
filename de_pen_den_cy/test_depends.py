import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

@pytest.fixture(scope='module')
def setup():
    driver=webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)
    yield driver
    driver.close()

@pytest.mark.dependency()
def test_login(setup):
    setup.find_element('id',"user-name").send_keys("standard_user")
    time.sleep(2)
    setup.find_element('id',"password").send_keys("")

