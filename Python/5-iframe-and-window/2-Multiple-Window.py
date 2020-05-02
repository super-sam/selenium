from selenium import webdriver
from selenium.webdriver.common.by import By


def get_num_of_windows():
    windows = driver.window_handles
    number_of_widows = len(windows)

    return number_of_widows


def switch_to_window_number(index):
    total_win = get_num_of_windows()

    if index >= total_win:
        raise AssertionError("There are {} window, Index {} will be out of bound".format(total_win, index))

    all_windows = driver.window_handles
    requested_window = all_windows[index]
    driver.switch_to.window(requested_window)


if __name__ == '__main__':
    global driver
    driver = webdriver.Chrome()
    try:
        url = "http://corporate.walmart.com"

        driver.get(url)
        link_careers_element = driver.find_element(By.XPATH, "/html/body/footer/div[2]/div[1]/nav/ul/li[7]/div/div/a")
        link_careers_element.click()

        number_of_windows = get_num_of_windows()

        print("There are {} windows open".format(number_of_windows))

        switch_to_window_number(1)
        new_win_title = driver.title

        print("New title: {}".format(new_win_title))

    finally:
        driver.quit()

