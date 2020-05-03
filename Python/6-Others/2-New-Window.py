from selenium import webdriver
from selenium.webdriver.common.by import By


def get_link_url(element):
    tag_type = element.tag_name

    if tag_type != 'a':
        print("The element isn't link. Checking if it contains contains other elements or links within it")

        child_elements = element.find_elements(By.TAG_NAME, 'a')
        num_of_links = len(child_elements)
        if num_of_links == 0:
            raise AssertionError("Element isn't a link")
        elif num_of_links > 1:
            raise AssertionError("There are multiple Element. Please provide specific element")
        else:
            link_url = child_elements[0].get_attribute('href')
    else:
        link_url = element.get_attribute('href')

    return link_url


if __name__ == '__main__':
    global driver

    try:
        driver = webdriver.Chrome()
        browser = webdriver.Chrome()

        url = "http://www.amazon.in"
        driver.get(url)

        link_element = driver.find_element(By.XPATH, '//*[@id="navFooter"]/div[1]/div/div[7]/ul/li[7]')
        my_url = get_link_url(link_element)

        browser.get(my_url)
        print(browser.title)

        import pdb
        pdb.set_trace()

    finally:
        driver.quit()
        browser.quit()
