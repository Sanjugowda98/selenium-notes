import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

ac_obj=ActionChains(driver)
driver.get("https://www.myntra.com/")
time.sleep(2)

women=driver.find_element("xpath",'(//a[text()="Women"])[1]')
ac_obj.move_to_element(women).perform()
time.sleep(2)

kids=driver.find_element("xpath",'(//a[text()="Kids"])[1]')
ac_obj.move_to_element(kids).perform()
time.sleep(2)


