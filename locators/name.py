import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.saucedemo.com/")
driver.find_element("name","user-name").send_keys("sanju")
time.sleep(2)