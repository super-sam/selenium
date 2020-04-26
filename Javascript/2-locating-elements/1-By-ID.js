const { Builder, By } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.selenium.dev/documentation/en/');
        const x = await driver.findElement(By.id('the-selenium-browser-automation-project'));
        console.log(await x.getText());
    } finally {
        driver.quit()
    }
})()