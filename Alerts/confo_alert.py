import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")

########Accept###########
# time.sleep(2)
# driver.find_element("xpath",'//button[text()="Confirmation Alert"]').click()
# alert_obj=driver.switch_to.alert
# time.sleep(2)
# alert_obj.accept()


#########dismis#######
# driver.find_element("xpath",'//button[text()="Confirmation Alert"]').click()
# alert_obj=driver.switch_to.alert
# time.sleep(2)
# alert_obj.dismiss()
