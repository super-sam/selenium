from selenium import webdriver

if __name__ == "__main__":
    driver = webdriver.Chrome()

    try:
        # NOTE: Run the sample.html in localhost before running this 
        url = "http://127.0.0.1:5500/Python/5-iframe-and-window/sample-iframe-main.html"
        
        driver.get(url)

        # find the paragraph outside the iframe
        p = driver.find_element_by_id('p-out')
        paragraph = p.text
        print(paragraph)

        # find the iframe element and switch focus to the iframe
        first_frame = driver.find_element('id', 'login-frame')
        driver.switch_to.frame(first_frame)

        # find username element within the iframe
        username = driver.find_element('id','username')
        username.send_keys('testuser')

        # witch focus back to the main page
        driver.switch_to.default_content()
        heading = driver.find_element('id', 'hh')
        print(heading.text)

        # find the second frame and switch focus to it
        second_frame = driver.find_element('id', 'ad-frame')
        driver.switch_to.frame(second_frame)
        image_link = driver.find_element('id', 'ad_image')
        print(image_link.get_attribute('src'))
        
        import pdb
        pdb.set_trace()

    finally:
        driver.quit()