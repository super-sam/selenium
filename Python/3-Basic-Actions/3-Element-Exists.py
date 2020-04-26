from selenium import webdriver

def element_exists(locator_attribute, locator_text):
    """
    Description: Find the element and returns true or false if element is found or not

    (str, str) => bool
    """
    possible_attributes = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector"]

    if not locator_attribute in possible_attributes:
        return False
    
    try:
        driver.find_element(locator_attribute, locator_text)
        return True
    except:
        return False

def assert_element_exists(locator_attribute, locator_text):
    if not element_exists(locator_attribute, locator_text):
        raise AssertionError("The requested with '%s' of '%s' doesn't exist" % (locator_attribute, locator_text))
    return True

driver = webdriver.Chrome()

try:
    url = "https://www.w3schools.com/"
    driver.get(url)
    if assert_element_exists('id', 'mySidenav'):
        print("Found %s of %s " % ('id', 'mySidenav'))
    
    if assert_element_exists('id', 'InvalidId'):
        print("Found %s of %s " % ('id', 'InvalidId'))

except Exception as e:
    print("Error: %s " % str(e))
finally:
    driver.quit()



