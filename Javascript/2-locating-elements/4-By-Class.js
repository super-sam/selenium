const { Builder, By} = require('selenium-webdriver');

(async function(){
    const driver = new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.selenium.dev/')
        /**
         * Fetch the below DOM node
         * <div class="download-button-container">
         *   <a href="/downloads">
         *     <div class="download-button webdriver"><b>DOWNLOAD</b></div>
         *   </a>
         * </div>
         */
        let my_element = await driver.findElement(By.className("download-button-container"));
        console.log(await my_element.getText());
    } finally {
        await driver.quit()
    }

})();
