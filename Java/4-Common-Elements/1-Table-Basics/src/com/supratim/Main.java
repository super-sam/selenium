package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;
import org.openqa.selenium.json.Json;

import java.util.List;
import java.util.Dictionary;
import java.util.Hashtable;

public class Main {
    private static WebDriver driver;
    private static String url;

    public static int getNumberOfTableRows(WebElement my_table){
        List<WebElement> all_rows = my_table.findElements(By.tagName("tr"));
        return all_rows.size();
    }

    private static boolean assertNumberOfRowInTable(WebElement my_table, int expected_num_rows){
        int actual_num_rows = getNumberOfTableRows(my_table);
        if (actual_num_rows != expected_num_rows){
            throw new AssertionError(String.format("Expected rows '%s' and Actual rows '%s' doesn't match.", actual_num_rows, expected_num_rows));
        }

        return true;
    }

    private static  boolean assertRowContainsText(WebElement my_table, String text_to_search, int row_num){
        List<WebElement> all_rows = my_table.findElements(By.tagName("tr"));

        WebElement my_row = all_rows.get(row_num);
        String actual_text = my_row.getText();


        if(!actual_text.contains(text_to_search)){
            throw new AssertionError(String.format("%s not found in %s at row %d", text_to_search, actual_text, row_num));
        }
        return true;
    }

    private static boolean assertColInRowContainsText(WebElement my_table, String text_to_search, int row_num, int col_num){
        assertRowContainsText(my_table, text_to_search, row_num);

        List<WebElement> all_rows = my_table.findElements((By.tagName("tr")));
        WebElement my_row = all_rows.get(row_num);

        List<WebElement> all_cols = my_row.findElements(By.tagName("td"));
        WebElement my_col = all_cols.get(col_num);

        String actual_text = my_col.getText();

        if(!actual_text.contains(text_to_search)){
            throw new AssertionError(String.format("'%s' not found in '%s' at row %d and col %d", text_to_search, actual_text, row_num, col_num));
        }
        return true;

    }

    public static void main(String[] args) {
        String id_to_search = "customers";
        String text_to_search = "UK";
        int row_to_search = 4;
        int col_to_search = 2;
        int rows  = 7;

        url = "http://www.w3schools.com/html/html_tables.asp";

        try {
            driver = new ChromeDriver();
            driver.get(url);

            WebElement table = driver.findElement(By.id(id_to_search));
            if(assertNumberOfRowInTable(table, rows)){
                System.out.println("Expected rows and Actual rows  match.");
            }

            if(assertColInRowContainsText(table, text_to_search, row_to_search, col_to_search)){
                System.out.println(String.format("%s found at row %d and col %d", text_to_search, row_to_search, col_to_search));
            }

        } finally {
            driver.quit();
        }

    }
}
