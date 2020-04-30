from selenium import webdriver



def get_number_of_table_rows(my_table):

    all_rows = my_table.find_elements_by_tag_name('tr')
    number_of_rows = len(all_rows)

    return number_of_rows


def assert_number_of_rows_in_table(my_table, expected_number_of_rows):
    actual_num_row = get_number_of_table_rows(my_table)

    if expected_number_of_rows != actual_num_row:
        raise AssertionError(
            "The number of row did not match. The acutal number is {} and the expected is {}".format(actual_num_row, expected_number_of_rows))

    return True


def assert_row_contains_text(my_table, text_to_check, row_number):
    all_rows = my_table.find_elements_by_tag_name('tr')
    my_row = all_rows[row_number]
    row_text = my_row.text

    if text_to_check not in row_text:
        raise AssertionError("The text {} is not in the row {}".format(text_to_check, row_number))
    else:
        print("The text {} is found in the row {}".format(text_to_check, row_number))
    return


def assert_col_in_row_contains_text(my_table, text_to_check, row_number=0, col_number=0):
    all_rows = my_table.find_elements_by_tag_name('tr')

    if row_number > len(all_rows):
        raise BaseException("The row number requested is more that available rows")

    my_row = all_rows[row_number]
    all_cols = my_row.find_elements_by_tag_name('td')
    my_col = all_cols[col_number]
    col_text = my_col.text

    if text_to_check not in col_text:
        raise AssertionError("The text {} is not in row {} col {}".format(text_to_check, row_number, col_number))
    else:
        print("The text {} is in row {} and column {}".format(text_to_check, row_number, col_number))

    return


if __name__ == '__main__':
    driver = webdriver.Chrome()

    url = "http://www.w3schools.com/html/html_tables.asp"
    try:
        driver.get(url)
        
        table = driver.find_element_by_id('customers')
        rows = get_number_of_table_rows(table)
        print("*****************")
        print(rows)
        print("*****************")

        assert_number_of_rows_in_table(table, 7)

        assert_col_in_row_contains_text(table, 'UK', row_number=4, col_number=2)
    except Exception as e:
        print(str(e))
    finally:
        driver.quit()
