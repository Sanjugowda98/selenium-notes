import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

opts=webdriver. ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(1)
date=driver.find_element("xpath",'//select[@name="birthday_day"]')
time.sleep(1)
select_obj=Select(date)
select_obj.select_by_index(2)
time.sleep(2)

