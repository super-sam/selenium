from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/documentation/en/")
x = driver.find_element_by_id('the-selenium-browser-automation-project')
y = driver.find_element('id', 'the-selenium-browser-automation-project')

print(x.text, y.text)

driver.quit()
