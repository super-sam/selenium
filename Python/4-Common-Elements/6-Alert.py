from selenium import webdriver
from selenium.webdriver.common.by import By

def is_alert_present(driver):
    try:
        driver.switch_to.alert
    except:
        return False
    
    return True

def assert_alert_present(driver):

    if not is_alert_present(driver):
        raise AssertionError("There is no alert present")

    return True


if __name__ == '__main__':
    driver = webdriver.Chrome()

    try:
        # NOTE: Run the sample.html in localhost before running this 
        url = "http://127.0.0.1:5500/Python/4-Common-Elements/prompt-sample.html"
        driver.get(url)
        if assert_alert_present(driver):
            print("Alert is present")
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()
