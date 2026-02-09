import time

from selenium import webdriver

opts=webdriver.ChromeOptions()
opts.add_experimental_option("detach",True)
driver=webdriver.Chrome(opts)
driver.get("https://www.kushals.com/?srsltid=AfmBOorfe9RrO_QqXb646cyVAENCIKJ-hsNv34tnL4CNvOit75l90JjY")
time.sleep(2)
driver.find_element("partial link text","Wedding Store").click()
time.sleep(2)