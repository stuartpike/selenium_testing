from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
import unittest
import xmlrunner

class GoogleTestCase(unittest.TestCase):

    def setUp(self):
        self.options = Options()
        self.options.add_argument("headless")
        self.service = Service(r"C:\Webdriver\msedgedriver.exe")
        self.driver = webdriver.Edge(options = self.options, service = self.service)
        self.driver.get("https://www.google.co.uk/")
        time.sleep(5)
    
    def test_google_images(self):
        images_link = self.driver.find_element(By.LINK_TEXT, 'Images')
        images_link.click()
        assert 'Google Images' in self.driver.title
        time.sleep(5)
    
    def test_google_search(self):
        search_box = self.driver.find_element(By.NAME, 'q')
        search_box.send_keys('Selenium with Python')
        search_box.submit()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
    
if __name__=='__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'), failfast=False, buffer=False, catchbreak=False, exit=False)
