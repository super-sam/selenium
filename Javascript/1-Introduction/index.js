const {Builder} = require('selenium-webdriver');

(async function() {
    let driver = await new Builder().forBrowser('chrome').build();
    try {
        // Navigate to Url
        await driver.get('http://www.python.org');
    }
    finally{
    }
})();
