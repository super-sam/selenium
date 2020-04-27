package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;


import java.lang.reflect.Method;

public class Main {
    public static WebDriver driver;
    public static void main(String[] args) {
	    driver = new ChromeDriver();
	    String url = "https://www.w3schools.com/";
	    driver.get(url);

	    try{
            String locator_fn = "id";
            String locator_text = "mySidenav";
	        if (assert_element_exist(locator_fn, locator_text)){
	            System.out.println(String.format("Found %s of %s ", locator_fn, locator_text));
            }

	        locator_text = "InvalidID";
            if (assert_element_exist(locator_fn, locator_text)){
                System.out.println(String.format("Found %s of %s ", locator_fn, locator_text));
            }

        } catch (AssertionError error){
            System.out.println(String.format("AssertionError: %s", error.getMessage()));
        } catch (Exception error){
            System.out.println(String.format("Error: %s", error.getMessage()));
        } finally {
	        driver.quit();
        }
    }

    private static boolean element_exist(String locator_fn, String locator_text){
        try{
            Method myMethod = By.class.getDeclaredMethod(locator_fn, String.class);
            WebElement my_element = driver.findElement((By) myMethod.invoke(null, locator_text));

        } catch (Exception e){
            System.out.println(e.getMessage());
            return false;
        }
        return true;


    }

    private static boolean assert_element_exist(String locator_fn, String locator_text){
        if(!element_exist(locator_fn, locator_text)){
            throw new AssertionError(String.format("The requested with '%s' of '%s' doesn't exist", locator_fn, locator_text));
        }
        return true;
    }
}
