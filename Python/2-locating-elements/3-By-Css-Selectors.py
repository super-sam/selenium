from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://selenium-python.readthedocs.io/")
my_class_element = driver.find_element_by_css_selector('.docutils.field-list')
print(my_class_element.text)

my_class_element = driver.find_element_by_css_selector('#selenium-with-python > table')
print(my_class_element.text)

my_class_element = driver.find_element_by_css_selector('table[frame="void"]')
print(my_class_element.text)

driver.quit()