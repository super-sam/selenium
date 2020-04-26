const {Builder, By} = require('selenium-webdriver');

(async function(){
    const driver = new Builder().forBrowser('chrome').build();

    try {
        const documentInitialised = () => driver.executeScript('return initialised');

        (await driver).get("https://starandread.com/store/namebook")
        
        (await driver).wait(() => documentInitialised(), 30000);

        let my_element = (await driver).findElement(By.id('select-product'));
        console.log(await my_element.getText());

    } finally {
        (await driver).quit();
    }

})();