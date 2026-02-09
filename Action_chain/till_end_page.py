import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

ac_obj=ActionChains(driver)
driver.get("https://www.myntra.com/")
time.sleep(2)

ac_obj.send_keys(Keys.END).perform()
time.sleep(2)

ac_obj.send_keys(Keys.HOME).perform()