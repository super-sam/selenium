const { Builder, By, Key } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        (await driver).manage().setTimeouts({implicit:30000});
        await driver.get('https://www.starandread.com/');
        /**
         * Go go google.com and search for "Selenium Webdriver"
         */
        const cart_element = await driver.findElement(By.xpath('//*[@id="bs-example-navbar-collapse-1"]/ul/li[3]/a')); 
        await cart_element.click();

        const title_element = await driver.findElement(By.xpath('/html/body/div[3]/center/h4'));
        console.info(await title_element.getText())
        
    } finally {
        await driver.quit()
    }
})()