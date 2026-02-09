import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
# path=r'C:\Users\smahes5x\PycharmProjects\selenium_training\files\Screenshot (41).png'
# driver.find_element("xpath",'//input[@id="singleFileInput"]').send_keys(path)
# time.sleep(2)

######multiple files##########
f1=r'C:\Users\smahes5x\PycharmProjects\selenium_training\files\Screenshot (41).png'
f2=r'C:\Users\smahes5x\PycharmProjects\selenium_training\files\Screenshot (42).png'
driver.find_element("xpath",'//input[@id="multipleFilesInput"]').send_keys(f'{f1}\n{f2}')
time.sleep(2)
