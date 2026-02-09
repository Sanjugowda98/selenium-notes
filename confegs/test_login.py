import time

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