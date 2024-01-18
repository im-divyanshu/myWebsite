from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/Samsung-Semi-Automatic-WT60R2000LL-TL-technology/dp/B08FMN5ZQM/ref=sr_1_9?keywords=washing+machine&sr=8-9")
price=driver.find_element(By.CLASS_NAME,value="a-price-whole")
print('The price is : ',price.text)
