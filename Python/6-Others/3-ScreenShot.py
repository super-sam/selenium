from selenium import webdriver
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    try:
        driver = webdriver.Chrome()

        url = "http://www.amazon.in"
        driver.get(url)
        driver.get_screenshot_as_file("screenshot.jpg")

    finally:
        driver.quit()
