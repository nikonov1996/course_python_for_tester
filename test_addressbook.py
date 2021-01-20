# Generated by Selenium IDE
from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()


  def test_addgroup(self):
    self.driver.get("http://localhost/addressbook/")
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "add new").click()
    self.driver.find_element(By.NAME, "firstname").click()
    self.driver.find_element(By.NAME, "firstname").send_keys("test_name")
    self.driver.find_element(By.NAME, "middlename").click()
    self.driver.find_element(By.NAME, "middlename").send_keys("test_midle_name")
    self.driver.find_element(By.NAME, "lastname").click()
    self.driver.find_element(By.NAME, "lastname").send_keys("test_last_name")
    self.driver.find_element(By.NAME, "nickname").click()
    self.driver.find_element(By.NAME, "nickname").send_keys("test_nikname")
    self.driver.find_element(By.NAME, "title").click()
    self.driver.find_element(By.NAME, "title").send_keys("test_title")
    self.driver.find_element(By.NAME, "company").click()
    self.driver.find_element(By.NAME, "company").send_keys("test_company")
    self.driver.find_element(By.NAME, "address").click()
    self.driver.find_element(By.NAME, "address").send_keys("test_address")
    self.driver.find_element(By.NAME, "home").click()
    self.driver.find_element(By.NAME, "home").send_keys("test_home")
    self.driver.find_element(By.NAME, "mobile").click()
    self.driver.find_element(By.NAME, "mobile").send_keys("890055533")
    self.driver.find_element(By.NAME, "work").click()
    self.driver.find_element(By.NAME, "work").send_keys("test_work")
    self.driver.find_element(By.NAME, "email").click()
    self.driver.find_element(By.NAME, "email").send_keys("test@test_company")
    self.driver.find_element(By.NAME, "bday").click()
    dropdown = self.driver.find_element(By.NAME, "bday")
    dropdown.find_element(By.XPATH, "//option[. = '17']").click()
    self.driver.find_element(By.NAME, "bday").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    dropdown = self.driver.find_element(By.NAME, "bmonth")
    dropdown.find_element(By.XPATH, "//option[. = 'October']").click()
    self.driver.find_element(By.NAME, "bmonth").click()
    self.driver.find_element(By.NAME, "aday").click()
    dropdown = self.driver.find_element(By.NAME, "aday")
    dropdown.find_element(By.XPATH, "//option[. = '15']").click()
    self.driver.find_element(By.NAME, "aday").click()
    self.driver.find_element(By.NAME, "amonth").click()
    dropdown = self.driver.find_element(By.NAME, "amonth")
    dropdown.find_element(By.XPATH, "//option[. = 'October']").click()
    self.driver.find_element(By.NAME, "amonth").click()
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(88)").click()
