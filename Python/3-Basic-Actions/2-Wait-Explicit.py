from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get('https://starandread.com/store/namebook')
    my_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located(('id', 'select-product')))
    print(my_element.text)
finally:
    driver.quit()
