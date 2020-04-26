const { Builder, By } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();

    try{
        await driver.get('https://selenium-python.readthedocs.io/')
        let my_class_element = await driver.findElement(By.css('.docutils.field-list'));
        console.log(await my_class_element.getText());

        my_class_element = await driver.findElement(By.css('#selenium-with-python > table'))
        console.log(await my_class_element.getText());

        my_class_element = await driver.findElement(By.css('table[frame="void"]'))
        console.log(await my_class_element.getText());
    } finally{
        driver.quit();
    }

})();