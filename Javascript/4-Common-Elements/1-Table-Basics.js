const { Builder, By } = require('selenium-webdriver');
const assert = require('assert');

const getNumberOfTableRows = async my_table => {
    const all_rows = (await my_table).findElements(By.tagName("tr"));
    const number_of_rows = (await all_rows).length;
    return number_of_rows
}

const assertNumberOfRowsInTable = async (my_table, expected_number_of_rows) => {
    const actual_num_rows = await getNumberOfTableRows(my_table);
    if (expected_number_of_rows != await actual_num_rows){
        throw new assert.AssertionError({
            actual: (await actual_num_rows),
            expected: expected_number_of_rows,
            operator: 'strictEqual',
            message: `The number of rows didn't match. The actual row is ${await actual_num_rows} and expect is ${expected_number_of_rows}`
        });
    }
    return true;
}

const assertRowContainsText = async (my_table, text_to_check, row_num) => {
    const all_rows = (await my_table).findElements(By.tagName('tr'))
    const my_row = (await all_rows)[row_num];
    const actual_text = (await my_row).getText();
    
    new assert.AssertionError({
        actual: await actual_text,
        expected: text_to_check,
        operator: 'strictEqual',
        message: `${text_to_check} not found at row ${row_num}`
    });
    
    return true
}

const assertColInRowContains = async (my_table, text_to_check, row_num, col_num) => {
    const all_rows = (await my_table).findElements(By.tagName('tr'))
    const my_row = (await all_rows)[row_num];
    const all_cols = (await my_row).findElements(By.tagName('td'));
    const my_col = (await all_cols)[col_num];

    const actual_text = (await my_col).getText()

    new assert.AssertionError({
        actual: await actual_text,
        expected: text_to_check,
        operator: 'strictEqual',
        message: `${text_to_check} not found at row ${row_num} and ${col_num}`
    });

    return true;

}

(async function(){
    let driver = new Builder().forBrowser('chrome').build();
    const config = {
        text_to_search : "UK",
        rows: 7,
        row_to_search: 4,
        col_to_search: 2
    }

    try {
        const url =  "http://www.w3schools.com/html/html_tables.asp";

        await driver.get(url);
        const table = await driver.findElement(By.id('customers'));
        
        const { rows, text_to_search, row_to_search, col_to_search} = config;

        if(await assertNumberOfRowsInTable(table, rows)){
            console.info(`Actual Row is equal to ${rows}`)
        }
        
        if(await assertRowContainsText(table, text_to_search, row_to_search)){
            console.info(`${text_to_search} found at ${row_to_search}`);
        }

        if(await assertColInRowContains(table, text_to_search, row_to_search, col_to_search)){
            console.info(`${text_to_search} found at row ${row_to_search} and col ${col_to_search}`)
        }
        
    } catch (error) {
        console.error(error);
    } finally {
        (await driver).quit()
    }
})();
