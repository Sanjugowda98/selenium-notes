import time
import pytest
from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)

@pytest.fixture(scope='class')
def setup():
    driver=webdriver.Chrome(opts)
    driver.get("https://demowebshop.tricentis.com/")
    time.sleep(2)
    yield driver
    driver.close()

class TestRegister:
    def test_reg(self,setup):
        setup.find_element("xpath",'//a[text()="Register"]').click()
        time.sleep(1)

    def test_gen_btn(self,setup):
        setup.find_element('id',"gender-male").click()


    def test_f_name(self,setup):
        setup.find_element('id',"FirstName").send_keys("sanju")


    def test_l_name(self,setup):
        setup.find_element('id',"LastName").send_keys("gowda")


    def test_email(self,setup):
        setup.find_element('id',"Email").send_keys("sanjugowda@gamil.com")


    def test_reg_pwd(self,setup):
        setup.find_element('id',"Password").send_keys("san@123")


    def test_con_pwd(self,setup):
        setup.find_element('id',"ConfirmPassword").send_keys("san@123")



class TestLogin:
    def test_login(self,setup):
        setup.find_element("xpath",'//a[text()="Log in"]').click()
        time.sleep(2)

    def test_email(self,setup):
        setup.find_element('id',"Email").send_keys("sanjugowda@gmail.com")
        time.sleep(2)

    def test_pwd(self,setup):
        setup.find_element('id',"Password").send_keys("san@123")
        time.sleep(2)




