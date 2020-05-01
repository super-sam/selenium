from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(30)

url = "https://www.starandread.com"

try:
    driver.get(url)
    '''
    Go go starandread.com and Click on "Cart" link on Navbar
    '''
    
    cart_element = driver.find_element(By.XPATH, '//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')
    cart_element.click()

    # Get the title of the cart
    title_element = driver.find_element(By.XPATH, '/html/body/div[3]/center/h4')
    print(title_element.text)

finally:
    driver.quit()