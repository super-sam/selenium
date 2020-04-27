package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import org.openqa.selenium.Keys;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();

        try{
            driver.get("https://www.google.com/");
            /**
             * Go go google.com and search for "Selenium Webdriver"
             */
            WebElement search_field = driver.findElement(By.name("q"));
            search_field.sendKeys("Selenium Webdriver");
            search_field.sendKeys(Keys.DOWN);
            search_field.sendKeys(Keys.DOWN);
            search_field.sendKeys(Keys.ENTER);

        } finally {
            driver.quit();
        }
    }
}
