from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.support import expected_conditions as EC
import time

class Keywords:
    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--incognito")
        self.driver = webdriver.Chrome(executable_path=binary_path, options=self.options)


    def inputText(self, fieldXpath):
        time.sleep(5)
        self.driver.find_element_by_xpath(fieldXpath).send_keys("johnemail@test.com")

    def clickBtn(self, fieldXpath):
        time.sleep(5)
        self.driver.find_element_by_xpath(fieldXpath).click()
        time.sleep(5)

    def checkElementPresence(self, fieldXpath):
        # self.wait.until(EC._element_if_visible(By.xpath(fieldXpath)))
        time.sleep(5)
        self.driver.find_element_by_xpath(fieldXpath)

