from selenium import webdriver;

driver = webdriver.Chrome()

try:
    driver.get('https://www.python.org/')
    '''
    Fetch the DOM node
    <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
        GO
    </button>
    '''
    my_element = driver.find_element('id', 'submit')

    my_element_class = my_element.get_attribute('class')        # value of class attribute in DOM node
    print("My Element class is '%s'" % my_element_class)

    my_element_title = my_element.get_attribute('title')        # value of title attribute in DOM node
    print("My Element title is '%s'" % my_element_title)


finally:
    driver.quit()