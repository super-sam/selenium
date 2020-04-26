package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.openqa.selenium.By;


public class Main {
    public static void main(String[] args) {
	    WebDriver driver = new ChromeDriver();
	    try{
	        driver.get("https://www.python.org");
	        WebElement my_link = driver.findElement(By.xpath("//*[@id=\"about\"]/a"));
	        System.out.println(my_link.getText());
        } finally {
            driver.quit();
        }
    }
}
