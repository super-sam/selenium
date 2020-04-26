const {Builder, By} = require('selenium-webdriver');

(async function(){
    const driver = new Builder().forBrowser('chrome').build();

    try {
        (await driver).manage().setTimeouts({implicit:30000});

        (await driver).get("https://starandread.com/store/namebook")

        let my_element = (await driver).findElement(By.id('select-product'));
        console.log(await my_element.getText());

    } finally {
        (await driver).quit();
    }

})();