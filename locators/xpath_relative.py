import time
""""#attributename=attributevalue
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.saucedemo.com/")
time.sleep(2)
driver.find_element("xpath",'//input[@placeholder="Username"]').send_keys("standard_user")
time.sleep(2)
driver.find_element("xpath",'//input[@id="password"]').send_keys("secret_sauce")
time.sleep(2)
driver.find_element("xpath",'//input[@name="login-button"]').click()
time.sleep(3)
driver.find_element("xpath",'//button[@type="button"]').click()
time.sleep(2)
driver.find_element("xpath",'//a[@id="logout_sidebar_link"]').click()"""

#using text

"""from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.flipkart.com/")
time.sleep(2)
driver.find_element("xpath",'//span[text()="TVs & Appliances"]').click()"""


#using group indexing when there are multiple occurance

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://www.facebook.com/r.php?entry_point=login")
# time.sleep(2)
# driver.find_element("xpath",'(//input[@type="text"])[1]').send_keys("sanju")
# time.sleep(2)
# driver.find_element("xpath",'(//input[@type="text"])[2]').send_keys("gowda")
# time.sleep(2)
# driver.find_element("xpath",'(//input[@type="text"])[5]').send_keys("984530224")

#using contains to locate the web-element using partial text of any tagname
# import time

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get("https://demowebshop.tricentis.com/ ")
# time.sleep(2)
# driver.find_element("xpath",'//a[contains(text(),"Books")]').click()
# time.sleep(2)

#back traversing

# from selenium import webdriver
# opts=webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get(r"C:\Users\smahes5x\PycharmProjects\selenium_training\files")
# time.sleep(2)
# driver.find_element("xpath",'//td[text()="Python"]/..//input[@type="checkbox"]').click()











