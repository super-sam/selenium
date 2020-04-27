const { Builder, By, Key } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.google.com/');
        /**
         * Go go google.com and search for "Selenium Webdriver"
         */
        const my_element = await driver.findElement(By.name('q'));
        await my_element.sendKeys("Selenium Webdriver");
        await my_element.sendKeys(Key.DOWN);
        await my_element.sendKeys(Key.DOWN);
        await my_element.sendKeys(Key.ENTER);
    } finally {
        await driver.quit()
    }
})()