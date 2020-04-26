from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pdb

driver = webdriver.Chrome()

url = "https://www.google.com"

try:
    driver.get(url)
    search_field = driver.find_element('name', 'q')
    search_field.send_keys('Selenium Webdriver')
    pdb.set_trace()  # Enter 'c' to continue

    search_field.send_keys(Keys.DOWN)
    search_field.send_keys(Keys.DOWN)
    pdb.set_trace()  # Enter 'c' to continue

    search_field.send_keys(Keys.ENTER)
    pdb.set_trace()  # Enter 'c' to continue
finally:
    driver.quit()