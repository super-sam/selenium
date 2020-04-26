from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('https://selenium.dev/documentation/en/')

    '''
    Fetch the below DOM node
    <a href="//www.w3.org/TR/webdriver/" class="highlight">W3C WebDriver specification</a>
    '''
    my_link = driver.find_element_by_link_text("W3C WebDriver specification")

    # Access the attributes value
    print(my_link.get_attribute('href'))
    my_link.click()
finally:
    driver.quit()
