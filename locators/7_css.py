import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
"""driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.find_element("css selector",'input[placeholder="Username"]').send_keys("standard_user")
time.sleep(2)"""
driver.get("https://www.facebook.com/r.php?entry_point=login")