from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
import time


code = input("Enter 22-digit code: ")

global driver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.pandaguestexperience.com/')
driver.find_element_by_id('CN1').send_keys(code)
driver.find_element_by_id('NextButton').click()
time.sleep(5)

driver.find_element_by_id('R000002.5').click()
driver.find_element_by_id('NextButton').click()
time.sleep(5) 

driver.find_element_by_id('R000008.5').click()
driver.find_element_by_id('R000018.5').click()
driver.find_element_by_id('R000013.5').click()
driver.find_element_by_id('R000012.5').click()
driver.find_element_by_id('R000287.5').click()
driver.find_element_by_id('R000010.5').click()
driver.find_element_by_id('NextButton').click()
time.sleep(5)

