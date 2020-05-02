from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

if __name__ == '__main__':
    driver = webdriver.Chrome()
    import pdb

    try:
        url = "http://www.amazon.com"
        driver.get(url)
        my_dropdown = Select(driver.find_element(By.ID, 'searchDropdownBox'))
        my_dropdown.select_by_visible_text("Books")

        pdb.set_trace()
        
        my_dropdown.select_by_value("search-alias=instant-video")
        pdb.set_trace()

    finally:
        driver.quit()
