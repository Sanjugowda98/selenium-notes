import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
opts=webdriver.ChromeOptions()

############Using timesleeep for 30 sec###################

# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.get(r"C:\Users\smahes5x\PycharmProjects\selenium_training\files\loading.html")
# time.sleep(30)
# driver.find_element("name","fname").send_keys('sanju')
# time.sleep(1)
# driver.find_element("name","lname").send_keys('gowdah')

##############using implicit wait##################
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# driver.implicitly_wait(30)
# driver.get(r"C:\Users\smahes5x\PycharmProjects\selenium_training\files\loading.html")
# driver.find_element("name","fname").send_keys('sanju')
# time.sleep(1)
# driver.find_element("name","lname").send_keys('gowdah')

###########Explicitly wait##############
# opts.add_experimental_option("detach",True)
# driver=webdriver.Chrome(opts)
# wait_obj=WebDriverWait(driver,30)
# driver.get(r'C:\Users\smahes5x\PycharmProjects\selenium_training\files\loading.html')
# wait_obj.until(EC.visibility_of_element_located(('xpath','//div[contains(text()," FirstName")]')))
# driver.find_element("name","fname").send_keys('sanju')
# time.sleep(1)
# driver.find_element("name","lname").send_keys('gowda')



