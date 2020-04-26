from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org")
my_link = driver.find_element_by_xpath('//*[@id="about"]/a')
print(my_link.text)

driver.quit()