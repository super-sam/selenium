from selenium import webdriver

if __name__ == '__main__':
    global driver
    try:
        driver = webdriver.Chrome()
        url = "https://www.google.com"

        driver.get(url)

        win_size = driver.get_window_size()     # It returns a dict with 'width' and 'height' key
        print(win_size)

        driver.set_window_size(width=400, height=400)
        new_win_size = driver.get_window_size()
        print(new_win_size)

        import pdb
        pdb.set_trace()

        win_loc = driver.get_window_position()  # It returns a dict
        print(win_loc)

        driver.set_window_position(x=300, y=300)
        new_win_loc = driver.get_window_position()
        print(new_win_loc)
        pdb.set_trace()

    finally:
        driver.quit()