from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
try:
    driver.get('https://starandread.com/store/namebook')
    my_element = driver.find_element_by_id('select-product')
    print(my_element.text)
finally:
    driver.quit()
