from selenium import webdriver
from selenium.webdriver.common.by import By

def assert_element_is_checkbox(element):
    my_element_type = element.get_attribute('type')

    if my_element_type != 'checkbox':
        raise AssertionError("Element isn't a checkbox")

    return True

def is_checkbox_selected(element):
    assert_element_is_checkbox(element)

    return element.is_selected()

def assert_checkbox_is_selected(element):
    if not is_checkbox_selected(element):
        raise AssertionError("Element is no selected")

    return True

def assert_checkbox_is_enabled(element):
    assert_element_is_checkbox(element)

    if not element.is_enabled():
        raise AssertionError("Checkbox isn't enabled")


if __name__ == '__main__':
    driver = webdriver.Chrome()
    import pdb

    try:
        # NOTE: Run the sample.html in localhost before running this script
        url = "http://127.0.0.1:5500/Python/4-Common-Elements/sample.html"
        driver.get(url)
        
        java_element = driver.find_element(By.NAME, 'java')
        print(is_checkbox_selected(java_element))
        assert_checkbox_is_enabled(java_element)

        php_element = driver.find_element(By.NAME, 'php')
        print(php_element.is_enabled())


    finally:
        driver.quit()
