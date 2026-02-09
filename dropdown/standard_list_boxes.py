import time
from selenium import  webdriver
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)

driver.get(r'file:///C:/Users/smahes5x/PycharmProjects/selenium_training/files/demo.html')
time.sleep(2)
#####SINGLE SELECT######
# cars=driver.find_element("xpath",'//select[@id="standard_cars"]')

#####MULTIPLE SELECT####
listboxes=driver.find_element("xpath",'//select[@id="multiple_cars"]')
select_obj=Select(listboxes)
select_obj.select_by_index(4)
time.sleep(1)
select_obj.select_by_index(1)
time.sleep(1)
select_obj.select_by_index(2)
time.sleep(2)
select_obj.select_by_value("aud")
time.sleep(2)
select_obj.select_by_value("bmw")
time.sleep(2)
select_obj.select_by_visible_text("Mercedes")
time.sleep(1)
print(select_obj.is_multiple)

# select_obj.deselect_by_index(4)
# time.sleep(1)

all_ele=select_obj.all_selected_options
for ele in all_ele:
    print(ele.text)




