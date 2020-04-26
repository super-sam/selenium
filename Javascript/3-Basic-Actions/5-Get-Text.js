const { Builder, By } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.w3schools.com/default.asp');
        const my_left_nav = await driver.findElement(By.className('w3-bar-block'));
        const left_nav_text = await my_left_nav.getText();
        console.log(left_nav_text);
    } finally {
        driver.quit()
    }
})()