import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

ac_obj=ActionChains(driver)
driver.get("https://www.myntra.com/")
time.sleep(2)

ele=driver.find_element("xpath",'//p[text()=" USEFUL LINKS "]')
ac_obj.scroll_to_element(ele).perform()