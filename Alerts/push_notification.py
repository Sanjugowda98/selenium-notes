import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
opts.add_argument("--disable-notifications")
driver=webdriver.Chrome(opts)
driver.get("https://www.irctc.co.in/nget/train-search")
time.sleep(2)