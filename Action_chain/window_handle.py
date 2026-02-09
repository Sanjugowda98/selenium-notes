import time
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)

handle=driver.window_handles
print(handle)

driver.find_element("xpath",'//a[text()="YouTube"]').click()
time.sleep(2)

parent_handle=driver.current_window_handle
time.sleep(2)

handles=driver.window_handles
print(handles)

for handle in handles:
    driver.switch_to.window(handle)
    if 'youtube' in driver.current_url:
        driver.find_element("css selector",'input[name="search_query"]').send_keys("python selenium")
        time.sleep(1)

driver.switch_to.window(parent_handle)
time.sleep(2)



