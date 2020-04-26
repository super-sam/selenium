package com.supratim;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class Main {

    public static void main(String[] args) {
        WebDriver driver = new ChromeDriver();

        try{
            driver.get("http://www.python.org");
        } finally {
            
        }
    }
}
