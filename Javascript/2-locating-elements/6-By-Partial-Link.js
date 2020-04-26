const {Builder, By} = require('selenium-webdriver');

(async function(){
    const driver = new Builder().forBrowser('chrome').build();

    try {
        (await driver).get("https://www.selenium.dev/")

        /**
         * Fetch the all the Link DOM node with text containing "DOWNL"
         */
        
        let my_links = (await driver).findElements(By.partialLinkText("DOWNL"));
        for (let my_link of await my_links){
            let my_href = (await my_link).getAttribute('href');
            console.info(await my_href);
        }

    } finally {
        (await driver).quit();
    }

})();