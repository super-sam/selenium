const {Builder, By} = require('selenium-webdriver');

(async function(){
    const driver = new Builder().forBrowser('chrome').build();

    try {
        (await driver).get("https://selenium.dev/documentation/en/")

        /**
         * Fetch the below DOM node
         * <a href="//www.w3.org/TR/webdriver/" class="highlight">W3C WebDriver specification</a>
         */
        let my_link = (await driver).findElement(By.linkText("W3C WebDriver specification"));
        let my_href = (await my_link).getAttribute('href');
        console.info(my_href);

        (await my_link).click();
       

    } finally {
        (await driver).quit();
    }

})();