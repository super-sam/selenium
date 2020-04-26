from selenium import webdriver

def element_visible(element):
    """
    Description: Find the element and returns true or false if element is found or not

    (Selenium) => bool
    """

    if element.is_displayed():
        return True
    else:
        return False
    
def assert_element_visible(element):
    if not element_visible(element):
        raise AssertionError("The requested element doesn't exist")
    return True


driver = webdriver.Chrome()

try:
    url = "https://www.w3schools.com/"
    driver.get(url)
    my_element = driver.find_element('id', 'mySidenav')
    if assert_element_visible(my_element):
        print("%s of %s is Visible" % ('id', 'mySidenav'))
    
    my_element = driver.find_element('id', 'navbtn_tutorials')
    if assert_element_visible(my_element):
        print("%s of %s is Visible" % ('id', 'navbtn_tutorials'))
    

except Exception as e:
    print("Error: %s " % str(e))
finally:
    driver.quit()