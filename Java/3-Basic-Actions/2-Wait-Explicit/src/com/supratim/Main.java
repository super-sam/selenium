package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;

import java.time.Duration;
import java.lang.reflect.Method;


public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
//            driver.get("https://www.starandread.com/store/namebook");
//            WebElement my_element = new WebDriverWait(driver, Duration.ofSeconds(30))
//                    .until(ExpectedConditions.presenceOfElementLocated(By.id("select-product")));
//            System.out.println(my_element.getText());

            boolean hasMethod = false;
            Method[] methods = By.class.getMethods();
            for (Method m : methods) {
                System.out.println(m.getName());

            }
        } finally {
            driver.quit();
        }

    }
}
