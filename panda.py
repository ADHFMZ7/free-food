from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType


code = input("Enter 22-digit code: ")

global driver

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://www.pandaguestexperience.com/')

driver.find_element_by_id('CN1').send_keys(code)

