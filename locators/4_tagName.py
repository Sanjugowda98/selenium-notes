import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.amazon.in/")
time.sleep(2)
driver.find_element("tag name","input").send_keys("shoes")
time.sleep(2)