import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
driver.get("https://admin:admin:@https://the-internet.herokuapp.com/basic_auth")
time.sleep(2)

