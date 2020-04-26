package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import java.util.List;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://www.selenium.dev/");
            /*
                Fetch the all the Link DOM node with text containing "DOWNL"
            */
            List<WebElement> my_class_elements = driver.findElements(By.partialLinkText("DOWNL"));

            for (WebElement element: my_class_elements) {
                System.out.println(element.getText());
            }
        } finally {
            driver.quit();
        }

    }
}
