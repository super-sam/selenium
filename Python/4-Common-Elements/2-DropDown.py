from selenium import webdriver
from selenium.webdriver.common.by import By

def assert_element_is_dropdown(element):
    if element.get_attribute('type') not in ['select-one', 'select-multi']:
        raise AssertionError('The element isn\'t a dropdown')

    return True

def select_from_dropdown_by_visible_text(element, select_text):
    assert_element_is_dropdown(element)

    all_options = element.find_elements(By.TAG_NAME, 'option')

    for option in all_options:
        option_text = option.text

        if option_text == select_text:
            option.click()
            return
    
    raise AssertionError("The requested option '{}' was not found in the dropdown".format(select_text))
        

def select_from_dropdown_by_value(element, select_value):
    assert_element_is_dropdown(element)

    all_options = element.find_elements(By.TAG_NAME, 'option')

    for option in all_options:
        option_value = option.get_attribute('value')

        if option_value == select_value:
            option.click()
            return True
    
    raise AssertionError("The requested value '{}' was not found in the dropdown".format(select_value))


if __name__ == '__main__':
    driver = webdriver.Chrome()

    try:
        url = "http://www.amazon.com"
        driver.get(url)
        my_dropdown = driver.find_element(By.ID, 'searchDropdownBox')

        select_from_dropdown_by_visible_text(my_dropdown, 'Books')
        import pdb
        pdb.set_trace()
    finally:
        driver.quit()
