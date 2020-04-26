from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://www.w3schools.com/default.asp')
    my_left_nav = driver.find_element_by_class_name('w3-bar-block')
    left_nav_text = my_left_nav.text

    print(left_nav_text)

finally:
    driver.quit()
