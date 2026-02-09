
import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver=webdriver.Chrome(opts)
driver.get("https://www.facebook.com/r.php?entry_point=login")
time.sleep(2)
driver.find_element("class name","xr2eeqj.xwyjyys.x1al4vs7.xmper1u.xzwoauc.x193iq5w.x6ikm8r.x10wlt62.x47corl.x10l6tqk.xlyipyv.x1d7kzl9.xii2z7h.x11xpdln.xuxw1ft.x1hp4nu4.xcvok8t.x1woyocn.x1kf5lb5.x183l01m.x1d72o.x1a1m0xk").send_keys('9845302204')
time.sleep(2)
















































