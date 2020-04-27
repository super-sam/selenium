const { Builder, By } = require('selenium-webdriver');
const { expect } = require('chai');

describe('DefaultTest', () => {
    const driver = new Builder().forBrowser('chrome').build();

    it('should go to Python.org and get the link text', async () => {
        await driver.get('https://www.python.org');
        let my_link = await driver.findElement(By.xpath('//*[@id="about"]/a'));
        let my_text = await my_link.getText()
        expect(my_text).to.equal("About");
    });

    after(async () => driver.quit());
});
