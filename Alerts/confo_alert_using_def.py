import time
from selenium import webdriver
opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)


def handle_alerts(userinput):
    alert_obj=driver.switch_to.alert
    if userinput=='accept':
        alert_obj.accept()
    elif userinput=="dismiss":
        alert_obj.dismiss()


driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(2)
driver.find_element("xpath",'//button[text()="Confirmation Alert"]').click()
time.sleep(2)
handle_alerts("accept")
time.sleep(2)
driver.find_element("xpath",'//button[text()="Confirmation Alert"]').click()
time.sleep(2)
handle_alerts("dismiss")
time.sleep(2)



