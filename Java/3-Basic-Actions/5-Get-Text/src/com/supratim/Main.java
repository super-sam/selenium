package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://www.w3schools.com/default.asp");

            WebElement my_class_element = driver.findElement(By.className("w3-bar-block"));

            System.out.println(my_class_element.getText());
        } finally {
            driver.quit();
        }

    }
}
