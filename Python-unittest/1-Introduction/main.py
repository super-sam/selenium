import unittest
from selenium import webdriver

class MainSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    
    def test_openURL(self):
        self.driver.get('http://www.python.org')
    
    def tearDown(self):
        self.driver.quit()
    

if __name__ == "__main__":
    unittest.main()