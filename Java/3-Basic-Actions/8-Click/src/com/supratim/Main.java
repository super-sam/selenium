package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.concurrent.TimeUnit;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        driver.manage().timeouts().implicitlyWait(30, TimeUnit.SECONDS);

        try{
            driver.get("https://www.starandread.com/");
            /**
             * Go go google.com and search for "Selenium Webdriver"
             */
            WebElement cart_element = driver.findElement(By.xpath("//*[@id=\"bs-example-navbar-collapse-1\"]/ul/li[3]/a"));
            cart_element.click();

            WebElement title_element = driver.findElement(By.xpath("/html/body/div[3]/center/h4"));
            System.out.println((title_element.getText()));

        } finally {
            driver.quit();
        }
    }
}
