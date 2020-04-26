const { Builder, By }  = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.python.org');
        let my_link = await driver.findElement(By.xpath('//*[@id="about"]/a'));
        console.log(await my_link.getText());
    } finally {
        driver.quit();
    }
})();