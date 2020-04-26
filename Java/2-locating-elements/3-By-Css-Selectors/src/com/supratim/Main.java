package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
	    WebDriver driver = new ChromeDriver();
	    try {
            driver.get("https://selenium-python.readthedocs.io/");
            WebElement my_class_element = driver.findElement(By.cssSelector(".docutils.field-list"));

            System.out.println(my_class_element.getText());
        } finally {
            driver.quit();
        }

    }
}
