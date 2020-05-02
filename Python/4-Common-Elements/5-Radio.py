from selenium import webdriver
from selenium.webdriver.common.by import By

def assert_element_is_radio(element):
    my_element_type = element.get_attribute('type')

    if my_element_type != 'radio':
        raise AssertionError("Element isn't a radio")

    return True

def assert_radio_is_selected(element):
    assert_element_is_radio(element)

    if not element.is_selected():
        raise AssertionError("Element is no selected")
    print("Radio is selected")    

    return True


def select_radio_by_value(elements, value):
    for element in elements:
        assert_element_is_radio(element)

        current_value = element.get_attribute('value')

        if current_value == value:
            element.click()
            return True
        
    raise AssertionError("'{}' not found in radios")

if __name__ == '__main__':
    driver = webdriver.Chrome()
    import pdb

    try:
        # NOTE: Run the sample.html in localhost before running this 
        url = "http://127.0.0.1:5500/Python/4-Common-Elements/sample.html"
        driver.get(url)
        pdb.set_trace()
        my_radios = driver.find_elements(By.NAME, 'age_grp')
        select_radio_by_value(my_radios, "31-40")
        pdb.set_trace()
        


    finally:
        driver.quit()
