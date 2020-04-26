from selenium import webdriver

driver = webdriver.Chrome()

try:
    driver.get('https://www.selenium.dev/')

    '''
    Fetch the all the Link DOM node with text containing "DOWNL"
    '''
    my_links = driver.find_elements_by_partial_link_text("DOWNL")
    for link in my_links:
        # Access the attributes value
        print(link.get_attribute('href'))

finally:
    driver.quit()
