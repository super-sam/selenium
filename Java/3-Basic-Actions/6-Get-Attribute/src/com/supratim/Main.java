package com.supratim;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();
        try {
            driver.get("https://www.python.org/");
            /*
                Fetch the DOM node
                <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
                    GO
                </button>
             */
            WebElement my_element = driver.findElement(By.id("submit"));

            String my_element_class = my_element.getAttribute("class"); // value of class attribute in DOM node
            System.out.println(my_element_class);

            String my_element_title = my_element.getAttribute("title"); // value of title attribute in DOM node
            System.out.println(my_element_title);

        } finally {
            driver.quit();
        }

    }
}
