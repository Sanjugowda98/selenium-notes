import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

ac_obj=ActionChains(driver)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
ele=driver.find_element("xpath",'//button[text()="Copy Text"]')
time.sleep(2)
ac_obj.double_click().perform()