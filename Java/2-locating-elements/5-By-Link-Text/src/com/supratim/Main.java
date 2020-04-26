package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://selenium.dev/documentation/en/");
            /*
                Fetch the below DOM node
                <a href="//www.w3.org/TR/webdriver/" class="highlight">W3C WebDriver specification</a>
             */
            WebElement my_class_element = driver.findElement(By.linkText("W3C WebDriver specification"));

            System.out.println(my_class_element.getAttribute("href"));
        } finally {
            driver.quit();
        }

    }
}
