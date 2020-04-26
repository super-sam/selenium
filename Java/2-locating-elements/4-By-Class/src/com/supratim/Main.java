package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://www.selenium.dev/");
            /*
            Fetch the below DOM node
            <div class="download-button-container">
                <a href="/downloads">
                <div class="download-button webdriver"><b>DOWNLOAD</b></div>
                </a>
            </div>
             */
            WebElement my_class_element = driver.findElement(By.className("download-button-container"));

            System.out.println(my_class_element.getText());
        } finally {
            driver.quit();
        }

    }
}
