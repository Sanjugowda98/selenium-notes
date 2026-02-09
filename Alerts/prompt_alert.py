import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element("xpath",'//button[text()="Prompt Alert"]').click()
time.sleep(2)
alert_obj=driver.switch_to.alert
alert_obj.send_keys('hi sanju')
alert_obj.accept()