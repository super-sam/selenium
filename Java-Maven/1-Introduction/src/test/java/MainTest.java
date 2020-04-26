import org.junit.AfterClass;
import org.junit.BeforeClass;
import  org.junit.Test;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.By;
import org.openqa.selenium.chrome.ChromeDriver;

import static org.junit.Assert.assertEquals;

public class MainTest {
    public static WebDriver driver;

    @BeforeClass
    public static void setUp(){
        driver = new ChromeDriver();
    }

    @Test
    public void checkTitle(){
        driver.get("https://www.python.org");
        WebElement my_element = driver.findElement(By.xpath("//*[@id=\"about\"]/a"));
        String my_string = my_element.getText();
        assertEquals("About", my_string);
    }

    @Test
    public void willFailTest(){
        driver.get("https://www.python.org");
        WebElement my_element = driver.findElement(By.xpath("//*[@id=\"about\"]/a"));
        String my_string = my_element.getText();
        assertEquals("NotAbout", my_string);
    }

    @AfterClass
    public static void tearDown(){
        driver.quit();
    }
}
