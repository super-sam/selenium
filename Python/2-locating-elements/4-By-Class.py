from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.selenium.dev/')

'''
Fetch the below DOM node
<div class="download-button-container">
    <a href="/downloads">
    <div class="download-button webdriver"><b>DOWNLOAD</b></div>
    </a>
</div>
'''
my_class_element = driver.find_element_by_class_name('download-button-container')

# Print the innerText of the DOM node fetched
print(my_class_element.text)

driver.quit()