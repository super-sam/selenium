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

        try {
            driver.get("https://starandread.com/store/namebook");
            /*
                Fetch the all the elements in Select-Product
            */
            WebElement my_class_element = driver.findElement(By.id("select-product"));
            System.out.println(my_class_element.getText());

        } finally {
            driver.quit();
        }

    }
}
