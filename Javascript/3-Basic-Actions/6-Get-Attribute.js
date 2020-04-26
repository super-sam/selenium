const { Builder, By } = require('selenium-webdriver');

(async function(){
    let driver = await new Builder().forBrowser('chrome').build();
    try{
        await driver.get('https://www.python.org/');
        /**
         * Fetch the DOM node
         * <button type="submit" name="submit" id="submit" class="search-button" title="Submit this Search" tabindex="3">
         * GO
         * </button>
         */
        const my_element = await driver.findElement(By.id('submit'));
        const my_element_class = await my_element.getAttribute('class');
        console.log(my_element_class);
        
        const my_element_title = await my_element.getAttribute('title');
        console.log(my_element_title);
    } finally {
        driver.quit()
    }
})()