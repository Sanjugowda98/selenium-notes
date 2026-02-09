import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
wait=WebDriverWait(driver,10)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.find_element("id","user-name").send_keys("standard_user")
time.sleep(1)
driver.find_element("id","password").send_keys("secret_sauce")
time.sleep(1)
driver.find_element("id","login-button").click()
try:
    wait.until(expected_conditions.url_contains("inventory"))
    print("successful login")
except:
    print("unsuccessful login")
